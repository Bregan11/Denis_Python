# Дан список размера N. 
# Найти максимальный из его локальных минимумов (локальный минимум — это элемент, который меньше любого из своих соседей).

N = int(input("Введите размер списка N: "))
numbers = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]

local_minima = [numbers[i] for i in range(1, N-1) if numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]]
max_local_min = max(local_minima) if local_minima else None

print("Максимальный локальный минимум:", max_local_min)