# Смоделировать простейший калькулятор, умеющий выполнять 4 основные арифметические операции.

# Импортируем необходимую библиотеку для обработки ошибок
import sys

def add(x, y):
    """Сложение двух чисел"""
    return x + y

def subtract(x, y):
    """Вычитание двух чисел"""
    return x - y

def multiply(x, y):
    """Умножение двух чисел"""
    return x * y

def divide(x, y):
    """Деление двух чисел с проверкой деления на ноль"""
    if y == 0:
        print("Ошибка! Деление на ноль.")
        sys.exit()
    return x / y

# Выбор операции
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Ошибка! Неверный ввод.")
