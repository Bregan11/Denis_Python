# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.

def InvertDigits(K):
    K = str(K)
    inverted = ''
    for digit in K:
        inverted = digit + inverted
    K = int(inverted)
    return K

numbers = [12345, 67890, 13579, 24680, 98765]
inverted_numbers = [InvertDigits(num) for num in numbers]

print(inverted_numbers)
