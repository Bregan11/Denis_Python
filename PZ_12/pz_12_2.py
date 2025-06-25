# Составить генератор (yield), который переведет символы строки из верхнего 
# регистра в нижний.

def to_lower_case(s):
    """Генератор, который переводит символы строки в нижний регистр."""
    for char in s:
        yield char.lower()

def main():
    # Запрос ввода от пользователя
    user_input = input("Введите строку для преобразования в нижний регистр: ")
    lower_case_generator = to_lower_case(user_input)
    print(''.join(lower_case_generator))

if __name__ == "__main__":
    main()
