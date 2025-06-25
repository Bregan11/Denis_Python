import tkinter as tk
from tkinter import ttk # Для Combobox и стилизации

class EventRegistrationForm:
    """
    Класс для создания GUI формы регистрации на мероприятие.
    """
    def __init__(self, master):
        self.master = master
        master.title("Event Registration")
        master.geometry("700x800") # Устанавливаем размер окна
        master.resizable(False, False) # Запрещаем изменение размера окна

        # Создаем градиентный фон (имитация, Tkinter не поддерживает градиенты напрямую)
        # Можно использовать Canvas для более сложного градиента, но для простоты
        # сделаем фон окна и фон фрейма.
        master.configure(bg="#8A2BE2") # Фиолетовый цвет для фона окна

        # Основной фрейм для формы (белый фон)
        self.form_frame = tk.Frame(master, bg="white", bd=2, relief="flat")
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6, relheight=0.8) # Размещаем по центру

        # Заголовок формы
        self.header_frame = tk.Frame(self.form_frame, bg="#333333", height=60)
        self.header_frame.pack(fill="x", pady=(0, 20)) # pady для отступа снизу
        self.header_label = tk.Label(self.header_frame, text="EVENT REGISTRATION FORM",
        fg="white", bg="#333333", font=("Arial", 16, "bold"))
        self.header_label.pack(pady=15)

        # Фрейм для содержимого формы
        self.content_frame = tk.Frame(self.form_frame, bg="white", padx=30, pady=20)
        self.content_frame.pack(fill="both", expand=True)

        # Использование grid для размещения элементов формы
        # Название
        tk.Label(self.content_frame, text="Name", font=("Arial", 10), bg="white").grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.first_name_entry = self.create_placeholder_entry(self.content_frame, "First Name")
        self.first_name_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self.last_name_entry = self.create_placeholder_entry(self.content_frame, "Last Name")
        self.last_name_entry.grid(row=1, column=1, sticky="ew")

        # Компания
        tk.Label(self.content_frame, text="Company", font=("Arial", 10), bg="white").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.company_entry = tk.Entry(self.content_frame, width=50, bd=1, relief="solid", font=("Arial", 10))
        self.company_entry.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Email
        tk.Label(self.content_frame, text="Email", font=("Arial", 10), bg="white").grid(row=4, column=0, sticky="w", pady=(10, 0))
        self.email_entry = tk.Entry(self.content_frame, width=50, bd=1, relief="solid", font=("Arial", 10))
        self.email_entry.grid(row=5, column=0, columnspan=2, sticky="ew")

        # Телефон
        tk.Label(self.content_frame, text="Phone", font=("Arial", 10), bg="white").grid(row=6, column=0, sticky="w", pady=(10, 0))
        self.area_code_entry = self.create_placeholder_entry(self.content_frame, "Area Code", width=10)
        self.area_code_entry.grid(row=7, column=0, sticky="ew", padx=(0, 10))
        self.phone_number_entry = self.create_placeholder_entry(self.content_frame, "Phone Number")
        self.phone_number_entry.grid(row=7, column=1, sticky="ew")

        # Тема (Subject) - используем Combobox для выпадающего списка
        tk.Label(self.content_frame, text="Subject", font=("Arial", 10), bg="white").grid(row=8, column=0, sticky="w", pady=(10, 0))
        self.subject_options = ["Choose option", "Option 1", "Option 2", "Option 3"]
        self.subject_var = tk.StringVar(self.content_frame)
        self.subject_var.set(self.subject_options[0]) # Устанавливаем значение по умолчанию

        # Стилизация Combobox
        style = ttk.Style()
        style.theme_use('clam') # Используем тему 'clam' для лучшей кастомизации
        style.configure("TCombobox",
                        fieldbackground="white",
                        background="white",
                        foreground="gray", # Цвет текста по умолчанию
                        selectbackground="white",
                        selectforeground="black",
                        bordercolor="gray",
                        lightcolor="gray",
                        darkcolor="gray",
                        arrowcolor="black",
                        padding=5)
        style.map('TCombobox',
        fieldbackground=[('readonly', 'white')],
        selectbackground=[('readonly', 'white')],
        selectforeground=[('readonly', 'black')],
        background=[('active', 'white')],
        foreground=[('!disabled', 'black')]) # Цвет текста при активном состоянии

        self.subject_combobox = ttk.Combobox(self.content_frame, textvariable=self.subject_var,
        values=self.subject_options, state="readonly",
        font=("Arial", 10), width=40)
        self.subject_combobox.grid(row=9, column=0, columnspan=2, sticky="ew")
        self.subject_combobox.set("Choose option") # Устанавливаем текст-заполнитель

        # Существующий клиент (Radio buttons)
        tk.Label(self.content_frame, text="Are you an existing customer?", font=("Arial", 10), bg="white").grid(row=10, column=0, sticky="w", pady=(20, 5))
        self.existing_customer_var = tk.StringVar(self.content_frame, value="No") # Значение по умолчанию

        # Создаем фрейм для радиокнопок, чтобы они были в одной строке
        radio_frame = tk.Frame(self.content_frame, bg="white")
        radio_frame.grid(row=11, column=0, columnspan=2, sticky="w")

        self.yes_radio = tk.Radiobutton(radio_frame, text="Yes", variable=self.existing_customer_var, value="Yes",
        bg="white", font=("Arial", 10),
        selectcolor="green", # Цвет индикатора при выборе
        activebackground="white", # Цвет фона при наведении
        indicatoron=True) # Показывает стандартный индикатор
        self.yes_radio.pack(side="left", padx=(0, 20))

        self.no_radio = tk.Radiobutton(radio_frame, text="No", variable=self.existing_customer_var, value="No",
        bg="white", font=("Arial", 10),
        selectcolor="gray", # Цвет индикатора при выборе
        activebackground="white",
        indicatoron=True)
        self.no_radio.pack(side="left")

        # Кнопка REGISTER
        self.register_button = tk.Button(self.content_frame, text="REGISTER",
        bg="#E74C3C", fg="white", font=("Arial", 12, "bold"),
        relief="flat", padx=20, pady=10,
        command=self.register_action)
        self.register_button.grid(row=12, column=0, columnspan=2, pady=(30, 0))

        # Настройка растягивания колонок для Entry по ширине
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)

    def create_placeholder_entry(self, parent, placeholder_text, width=None):
        """
        Создает Entry виджет с текстом-заполнителем.
        """
        entry = tk.Entry(parent, bd=1, relief="solid", font=("Arial", 10), width=width)
        entry.insert(0, placeholder_text)
        entry.config(fg='gray')

        def on_focus_in(event):
            if entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg='black')

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, placeholder_text)
                entry.config(fg='gray')

        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)
        return entry

    def register_action(self):
        """
        Функция, вызываемая при нажатии кнопки REGISTER.
        Здесь можно получить данные из полей.
        """
        first_name = self.first_name_entry.get() if self.first_name_entry.cget('fg') == 'black' else ""
        last_name = self.last_name_entry.get() if self.last_name_entry.cget('fg') == 'black' else ""
        company = self.company_entry.get()
        email = self.email_entry.get()
        area_code = self.area_code_entry.get() if self.area_code_entry.cget('fg') == 'black' else ""
        phone_number = self.phone_number_entry.get() if self.phone_number_entry.cget('fg') == 'black' else ""
        subject = self.subject_var.get()
        existing_customer = self.existing_customer_var.get()

        print("--- Данные регистрации ---")
        print(f"Имя: {first_name} {last_name}")
        print(f"Компания: {company}")
        print(f"Email: {email}")
        print(f"Телефон: ({area_code}) {phone_number}")
        print(f"Тема: {subject}")
        print(f"Существующий клиент: {existing_customer}")
        print("--------------------------")
        tk.messagebox.showinfo("Регистрация", "Форма отправлена! (Данные в консоли)")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventRegistrationForm(root)
    root.mainloop()

