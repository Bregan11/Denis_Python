# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.

def InvertDigits(K):
    reversed_number = 0
    while K > 0:
        last_digit = K % 10  # Извлекаем последнюю цифру
        reversed_number = reversed_number * 10 + last_digit  # Добавляем её к новому числу
        K = K // 10  # Удаляем последнюю цифру из K
    return reversed_number

# Пример использования функции для пяти данных целых чисел
numbers = [12345, 67890, 121314, 987654321, 1010101]
reversed_numbers = [InvertDigits(num) for num in numbers]

# Вывод результатов
for original, reversed in zip(numbers, reversed_numbers):
    print(f"Оригинальное число: {original}, Обратное число: {reversed}")

