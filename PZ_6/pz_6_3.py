# Дан список размера N и целое число K (1 < K < N). 
# Осуществить сдвиг элементов список вправо на K позиций 
# (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в AN, а исходное значение K последних элементов будет потеряно). 
# Первые K элементов полученного списка положить равными 0.

N = int(input("Введите размер списка N: "))
K = int(input("Введите целое число K (1 < K < N): "))
elements = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]

shifted_list = [0] * K + elements[:-K]
print("Сдвинутый список:", shifted_list)