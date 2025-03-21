# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Повторяющиеся элементы:
# Количество повторяющихся элементов:
# Элементы больше 5 увеличены в два раза:

import random
import os

# Папка, в которую сохраняются файлы
output_dir = 'PZ_11'

# Создаем последовательность из целых положительных и отрицательных чисел
numbers = [random.randint(-10, 10) for _ in range(20)]

# Пути к файлам внутри директории PZ_11
input_file_path = os.path.join(output_dir, 'numbers.txt')
output_file_path = os.path.join(output_dir, 'processed_numbers.txt')

# Сохраняем последовательность в текстовый файл
with open(input_file_path, 'w') as file:
    file.write(' '.join(map(str, numbers)))

# Выполняем требуемую обработку элементов
product = 1
for num in numbers:
    product *= num

repeated_elements = set([num for num in numbers if numbers.count(num) > 1])

doubled_elements = [num * 2 if num > 5 else num for num in numbers]

# Сохраняем результаты в новый текстовый файл
with open(output_file_path, 'w') as file:
    file.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
    file.write(f"Количество элементов: {len(numbers)}\n")
    file.write(f"Произведение элементов: {product}\n")
    file.write(f"Повторяющиеся элементы: {' '.join(map(str, repeated_elements))}\n")
    file.write(f"Количество повторяющихся элементов: {len(repeated_elements)}\n")
    file.write(f"Элементы больше 5 увеличены в два раза: {' '.join(map(str, doubled_elements))}\n")

input_file_path, output_file_path
