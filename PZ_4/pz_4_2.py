# Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
# деления, вывести все его цифры, начиная с самой правой (разряда единиц).

def print_digits(n):
    """
    Функция для вывода цифр целого числа, начиная с самой правой.
    
    :param n: Целое число больше 0
    """
    if n <= 0:
        raise ValueError("Число должно быть больше 0.")
    
    try:
        while n > 0:
            digit = n % 10  # Получаем последнюю цифру
            print(digit)    # Выводим цифру
            n //= 10        # Убираем последнюю цифру
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    try:
        number = int(input("Введите целое число больше 0: "))
        print_digits(number)
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
