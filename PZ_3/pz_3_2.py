# Смоделировать простейший калькулятор, умеющий выполнять 4 основные арифметические операции.

# Определение функций для каждой арифметической операции
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Ошибка: деление на ноль")
    return x / y

# Главная функция калькулятора
def calculator():
    print("Простой калькулятор")

    # Ввод чисел от пользователя
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выбор операции
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    # Выполнение операции в зависимости от выбора пользователя
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        try:
            print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError as e:
            print(e)
    else:
        print("Ошибка: неверный выбор операции")

# Запуск калькулятора
calculator()