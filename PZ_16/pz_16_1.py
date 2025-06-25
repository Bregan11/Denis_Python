# Создайте класс «Книга», который имеет атрибуты название, автор и количество
# страниц. Добавьте методы для чтения и записи книги.


class Book:
    """
    Класс, представляющий книгу.
    Имеет атрибуты: название, автор, количество страниц.
    """

    def __init__(self, title, author, page_count):
        """
        Конструктор класса Book.
        :param title: Название книги (строка).
        :param author: Автор книги (строка).
        :param page_count: Количество страниц в книге (целое число).
        """
        if not isinstance(title, str) or not title:
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author:
            raise ValueError("Автор книги должен быть непустой строкой.")
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self._title = title  # Используем _ для обозначения защищенных атрибутов
        self._author = author
        self._page_count = page_count

    # Методы для чтения (получения) атрибутов
    def get_title(self):
        """Возвращает название книги."""
        return self._title

    def get_author(self):
        """Возвращает автора книги."""
        return self._author

    def get_page_count(self):
        """Возвращает количество страниц в книге."""
        return self._page_count

    def read_book(self):
        """
        Имитирует "чтение" книги, выводя ее основные данные.
        """
        print(f"--- Чтение книги ---")
        print(f"Название: {self._title}")
        print(f"Автор: {self._author}")
        print(f"Количество страниц: {self._page_count}")
        print(f"--------------------")

    # Методы для записи (изменения) атрибутов
    def set_title(self, new_title):
        """
        Изменяет название книги.
        :param new_title: Новое название книги (строка).
        """
        if not isinstance(new_title, str) or not new_title:
            raise ValueError("Новое название книги должно быть непустой строкой.")
        self._title = new_title
        print(f"Название книги изменено на: '{new_title}'")

    def set_author(self, new_author):
        """
        Изменяет автора книги.
        :param new_author: Новый автор книги (строка).
        """
        if not isinstance(new_author, str) or not new_author:
            raise ValueError("Новый автор книги должен быть непустой строкой.")
        self._author = new_author
        print(f"Автор книги изменен на: '{new_author}'")

    def set_page_count(self, new_page_count):
        """
        Изменяет количество страниц в книге.
        :param new_page_count: Новое количество страниц (целое число).
        """
        if not isinstance(new_page_count, int) or new_page_count <= 0:
            raise ValueError("Новое количество страниц должно быть положительным целым числом.")
        self._page_count = new_page_count
        print(f"Количество страниц изменено на: {new_page_count}")

# Пример использования класса Book
if __name__ == "__main__":
    try:
        # Создание экземпляра книги
        my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 450)
        my_book.read_book()

        # Изменение атрибутов книги
        my_book.set_page_count(480)
        my_book.set_title("Мастер и Маргарита (Полное издание)")
        my_book.read_book()

        # Попытка создать книгу с некорректными данными
        # invalid_book = Book("", "Автор", 100) # Вызовет ValueError
        # invalid_book = Book("Название", "Автор", -50) # Вызовет ValueError

    except ValueError as e:
        print(f"Ошибка: {e}")