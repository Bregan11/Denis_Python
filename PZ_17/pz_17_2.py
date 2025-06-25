# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
# средние температуры по месяцам в году. Преобразовать информацию из строки в
# словарь, с использованием функции найти среднюю и минимальные температуры,
# результаты вывести на экран.
# Вариант 26, PZ №9


import tkinter as tk
from tkinter import messagebox

class TemperatureAnalyzerApp:
    """
    Класс для GUI-приприложения, анализирующего температуры.
    """
    def __init__(self, master):
        self.master = master
        master.title("Анализатор температур")
        master.geometry("500x350")
        master.resizable(False, False)

        self.temperature_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
        self.temperatures_dict = {}
        self.average_temp = None
        self.min_temp = None

        # Заголовок
        self.title_label = tk.Label(master, text="Анализ средних температур по месяцам",
        font=("Arial", 14, "bold"), pady=10)
        self.title_label.pack()

        # Отображение исходной строки
        self.input_label_text = tk.Label(master, text="Исходные данные:", font=("Arial", 10, "bold"))
        self.input_label_text.pack(pady=(10, 0))
        self.input_string_display = tk.Label(master, text=self.temperature_string,
        font=("Courier New", 10), wraplength=450, justify="center")
        self.input_string_display.pack(pady=(0, 10))

        # Кнопка для запуска анализа
        self.analyze_button = tk.Button(master, text="Выполнить анализ",
        command=self.perform_analysis,
        font=("Arial", 12), bg="#4CAF50", fg="white",
        relief="raised", padx=10, pady=5)
        self.analyze_button.pack(pady=20)

        # Отображение результатов
        self.result_frame = tk.Frame(master, bd=2, relief="groove", padx=20, pady=15)
        self.result_frame.pack(pady=10)

        self.avg_label = tk.Label(self.result_frame, text="Средняя температура: Не рассчитано",
        font=("Arial", 12))
        self.avg_label.pack(anchor="w", pady=5)

        self.min_label = tk.Label(self.result_frame, text="Минимальная температура: Не рассчитано",
        font=("Arial", 12))
        self.min_label.pack(anchor="w", pady=5)

    def parse_temperatures(self, temp_string):
        """
        Преобразует строку температур в словарь.
        Ключи - номера месяцев (1-12), значения - температуры.
        Возвращает год и словарь температур.
        """
        parts = temp_string.split()
        year_str = parts[0]
        year = int(year_str.replace('год', '')) # Извлекаем год

        temperatures = [int(t) for t in parts[1:]]
        
        if len(temperatures) != 12:
            raise ValueError("Ожидается 12 значений температур для 12 месяцев.")

        temp_dict = {i + 1: temperatures[i] for i in range(12)}
        return year, temp_dict

    def analyze_temperatures(self, temp_dict):
        """
        Находит среднюю и минимальную температуру из словаря.
        """
        if not temp_dict:
            return 0, 0 # Возвращаем 0, если словарь пуст

        temps = list(temp_dict.values())
        average = sum(temps) / len(temps)
        minimum = min(temps)
        return average, minimum

    def perform_analysis(self):
        """
        Выполняет полный цикл анализа и обновляет GUI.
        """
        try:
            year, self.temperatures_dict = self.parse_temperatures(self.temperature_string)
            self.average_temp, self.min_temp = self.analyze_temperatures(self.temperatures_dict)

            self.avg_label.config(text=f"Средняя температура: {self.average_temp:.2f}°C")
            self.min_label.config(text=f"Минимальная температура: {self.min_temp}°C")

            messagebox.showinfo("Анализ завершен", "Расчеты успешно выполнены!")

        except ValueError as e:
            messagebox.showerror("Ошибка данных", f"Произошла ошибка при обработке данных: {e}")
        except Exception as e:
            messagebox.showerror("Неизвестная ошибка", f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureAnalyzerApp(root)
    root.mainloop()

