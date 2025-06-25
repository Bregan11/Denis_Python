# Приложение для туристического агентства ТУР. Таблица Турист должна
# содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
# (Фамилия), Телефон, Название страны, Регион, Продолжительность поездки,
# Стоимость путевки.

import sqlite3
import sys

class TravelAgencyDB:
    """
    Класс для управления базой данных туристического агентства.
    Обеспечивает функционал по вводу, поиску, удалению и редактированию данных.
    """

    def __init__(self, db_name="travel_agency.db"):
        """
        Инициализирует подключение к базе данных и создает таблицу "Tourist", если она не существует.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self._create_table()
            print(f"Подключение к базе данных '{self.db_name}' успешно установлено.")
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            sys.exit(1) # Выход из программы при критической ошибке

    def _create_table(self):
        """
        Создает таблицу "Tourist" с необходимой структурой.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Tourist (
                    client_code INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name TEXT NOT NULL,
                    phone TEXT,
                    country_name TEXT NOT NULL,
                    region TEXT,
                    trip_duration INTEGER NOT NULL,
                    tour_cost REAL NOT NULL
                )
            """)
            self.conn.commit()
            print("Таблица 'Tourist' успешно создана или уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")
            sys.exit(1)

    def add_tourist(self, last_name, phone, country_name, region, trip_duration, tour_cost):
        """
        Добавляет новую запись о туристе в базу данных.
        """
        try:
            self.cursor.execute("""
                INSERT INTO Tourist (last_name, phone, country_name, region, trip_duration, tour_cost)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (last_name, phone, country_name, region, trip_duration, tour_cost))
            self.conn.commit()
            print(f"Турист '{last_name}' успешно добавлен.")
            return self.cursor.lastrowid # Возвращаем ID добавленной записи
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении туриста: {e}")
            return None

    def get_all_tourists(self):
        """
        Возвращает все записи из таблицы "Tourist".
        """
        try:
            self.cursor.execute("SELECT * FROM Tourist")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении всех туристов: {e}")
            return []

    def search_tourists(self, criteria, query_type):
        """
        Ищет туристов по заданным критериям.
        query_type:
            1 - по Коду клиента (client_code)
            2 - по Фамилии (last_name) с частичным совпадением
            3 - по Названию страны (country_name) с частичным совпадением
        """
        sql_queries = {
            1: "SELECT * FROM Tourist WHERE client_code = ?",
            2: "SELECT * FROM Tourist WHERE last_name LIKE ?",
            3: "SELECT * FROM Tourist WHERE country_name LIKE ?"
        }
        try:
            if query_type not in sql_queries:
                print("Неверный тип запроса для поиска.")
                return []

            sql = sql_queries[query_type]
            # Параметры для LIKE запросов должны быть обернуты в %
            params = (criteria,) if query_type == 1 else (f"%{criteria}%",)
            self.cursor.execute(sql, params)
            results = self.cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Ошибка при поиске туристов: {e}")
            return []

    def delete_tourist(self, criteria, query_type):
        """
        Удаляет туристов по заданным критериям.
        query_type:
            1 - по Коду клиента (client_code)
            2 - по Фамилии (last_name)
            3 - по Названию страны (country_name) и Региону (region)
        """
        sql_queries = {
            1: "DELETE FROM Tourist WHERE client_code = ?",
            2: "DELETE FROM Tourist WHERE last_name = ?",
            3: "DELETE FROM Tourist WHERE country_name = ? AND region = ?"
        }
        try:
            if query_type not in sql_queries:
                print("Неверный тип запроса для удаления.")
                return 0

            sql = sql_queries[query_type]
            if query_type == 3:
                # Для типа 3, criteria должен быть кортежем (country_name, region)
                if not isinstance(criteria, tuple) or len(criteria) != 2:
                    print("Для удаления по стране и региону, критерии должны быть кортежем (Название_страны, Регион).")
                    return 0
                params = criteria
            else:
                params = (criteria,)

            self.cursor.execute(sql, params)
            self.conn.commit()
            rows_affected = self.cursor.rowcount
            return rows_affected
        except sqlite3.Error as e:
            print(f"Ошибка при удалении туриста: {e}")
            return 0

    def update_tourist(self, client_code, new_value, query_type):
        """
        Редактирует информацию о туристе по Коду клиента.
        query_type:
            1 - обновить Телефон (phone)
            2 - обновить Стоимость путевки (tour_cost)
            3 - обновить Регион (region)
        """
        update_fields = {
            1: "phone",
            2: "tour_cost",
            3: "region"
        }
        try:
            if query_type not in update_fields:
                print("Неверный тип запроса для редактирования.")
                return 0

            field_name = update_fields[query_type]
            sql = f"UPDATE Tourist SET {field_name} = ? WHERE client_code = ?"
            self.cursor.execute(sql, (new_value, client_code))
            self.conn.commit()
            rows_affected = self.cursor.rowcount
            return rows_affected
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении туриста: {e}")
            return 0

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        if self.conn:
            self.conn.close()
            print("Соединение с базой данных закрыто.")

def display_results(header, results):
    """
    Вспомогательная функция для красивого вывода результатов.
    """
    print(f"\n--- {header} ---")
    if not results:
        print("Нет данных.")
        return

    # Заголовки столбцов
    print(f"{'Код клиента':<15} {'Фамилия':<20} {'Телефон':<15} {'Страна':<20} {'Регион':<15} {'Длительность':<15} {'Стоимость':<15}")
    print("-" * 115)
    # Вывод данных
    for t in results:
        print(f"{t[0]:<15} {t[1]:<20} {t[2]:<15} {t[3]:<20} {t[4]:<15} {t[5]:<15} {t[6]:<15.2f}")
    print("-" * 115)


if __name__ == "__main__":
    db = TravelAgencyDB(db_name="travel_agency_demo.db") # Используем другое имя БД для демонстрации

    # 1. Добавление тестовых данных
    print("\n--- Добавление тестовых данных ---")
    ivanov_id = db.add_tourist("Иванов", "89011234567", "Италия", "Ломбардия", 7, 1200.50)
    petrova_id = db.add_tourist("Петрова", "89022345678", "Испания", "Каталония", 10, 1500.00)
    sidorov_id = db.add_tourist("Сидоров", "89033456789", "Греция", "Крит", 14, 950.75)
    kozlova_id = db.add_tourist("Козлова", "89044567890", "Турция", "Анталия", 8, 800.00)
    smirnov_id = db.add_tourist("Смирнов", "89055678901", "Египет", "Шарм-эль-Шейх", 9, 1100.20)
    kuznetsova_id = db.add_tourist("Кузнецова", "89066789012", "Таиланд", "Пхукет", 12, 2000.00)
    volkov_id = db.add_tourist("Волков", "89077890123", "Вьетнам", "Нячанг", 11, 1800.00)
    morozova_id = db.add_tourist("Морозова", "89088901234", "Франция", "Париж", 5, 1300.00)
    novikov_id = db.add_tourist("Новиков", "89099012345", "Германия", "Бавария", 6, 1000.00)
    lebedeva_id = db.add_tourist("Лебедева", "89100123456", "Италия", "Тоскана", 7, 1400.00)

    display_results("Все туристы после добавления", db.get_all_tourists())

    # 2. Демонстрация операций поиска (3 запроса)
    print("\n--- Демонстрация поиска ---")

    # Поиск 1: По Коду клиента
    print("\nПоиск по Коду клиента (client_code = 2):")
    results_search_1 = db.search_tourists(petrova_id, 1)
    display_results("Результат поиска по Коду клиента", results_search_1)

    # Поиск 2: По Фамилии (LIKE 'Ив%')
    print("\nПоиск по Фамилии (LIKE 'Ив%'):")
    results_search_2 = db.search_tourists("Ив", 2)
    display_results("Результат поиска по Фамилии", results_search_2)

    # Поиск 3: По Названию страны (LIKE '%лан%')
    print("\nПоиск по Названию страны (LIKE '%лан%'):")
    results_search_3 = db.search_tourists("лан", 3)
    display_results("Результат поиска по Названию страны", results_search_3)

    # 3. Демонстрация операций редактирования (3 запроса)
    print("\n--- Демонстрация редактирования ---")

    # Редактирование 1: Обновить Телефон для Иванова
    print(f"\nОбновление телефона для Иванова (ID: {ivanov_id})...")
    rows_updated_1 = db.update_tourist(ivanov_id, "89991112233", 1)
    print(f"Обновлено записей: {rows_updated_1}")
    display_results("Иванов после обновления телефона", db.search_tourists(ivanov_id, 1))

    # Редактирование 2: Обновить Стоимость путевки для Петровой
    print(f"\nОбновление стоимости путевки для Петровой (ID: {petrova_id})...")
    rows_updated_2 = db.update_tourist(petrova_id, 1650.75, 2)
    print(f"Обновлено записей: {rows_updated_2}")
    display_results("Петрова после обновления стоимости", db.search_tourists(petrova_id, 1))

    # Редактирование 3: Обновить Регион для Сидорова
    print(f"\nОбновление региона для Сидорова (ID: {sidorov_id})...")
    rows_updated_3 = db.update_tourist(sidorov_id, "Аттика", 3)
    print(f"Обновлено записей: {rows_updated_3}")
    display_results("Сидоров после обновления региона", db.search_tourists(sidorov_id, 1))

    # 4. Демонстрация операций удаления (3 запроса)
    print("\n--- Демонстрация удаления ---")

    # Удаление 1: По Коду клиента (удаляем Козлову)
    print(f"\nУдаление Козловой (ID: {kozlova_id})...")
    rows_deleted_1 = db.delete_tourist(kozlova_id, 1)
    print(f"Удалено записей: {rows_deleted_1}")
    display_results("Проверка: Козлова после удаления", db.search_tourists(kozlova_id, 1))

    # Удаление 2: По Фамилии (удаляем Смирнова)
    print("\nУдаление Смирнова по фамилии...")
    rows_deleted_2 = db.delete_tourist("Смирнов", 2)
    print(f"Удалено записей: {rows_deleted_2}")
    display_results("Проверка: Смирнов после удаления", db.search_tourists("Смирнов", 2))

    # Удаление 3: По Названию страны и Региону (удаляем Лебедеву)
    print("\nУдаление Лебедевой по стране и региону (Италия, Тоскана)...")
    rows_deleted_3 = db.delete_tourist(("Италия", "Тоскана"), 3)
    print(f"Удалено записей: {rows_deleted_3}")
    display_results("Проверка: Лебедева после удаления", db.search_tourists("Лебедева", 2))

    display_results("Все туристы после всех операций", db.get_all_tourists())

    db.close()
    print("\nДемонстрация завершена.")
