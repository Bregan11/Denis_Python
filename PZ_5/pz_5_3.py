# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.

def InvertDigits(K):
    try:
        K = int(K)
        inverted = int(str(K)[::-1])
        return inverted
    except ValueError:
        return "Ошибка: Введите целое положительное число."

numbers = [12345, 67890, 54321, 98765, 13579]
inverted_numbers = [InvertDigits(num) for num in numbers]

print(inverted_numbers)
