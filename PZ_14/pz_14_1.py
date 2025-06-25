# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные 
# адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами, 
# а во второй – все остальные.  Посчитать количество полученных строк в каждом 
# файле.

import re

# Функция для чтения файла и разделения строк
def split_ip_addresses(input_file, output_file1, output_file2):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Регулярное выражение для поиска IP-адресов
    ip_pattern = re.compile(r'\b(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}\b')

    file1_lines = []
    file2_lines = []

    for line in lines:
        match = ip_pattern.search(line)
        if match:
            first_octet = int(match.group(1))
            second_octet = int(match.group(2))
            if first_octet != 0 and second_octet != 0:
                file1_lines.append(line)
            else:
                file2_lines.append(line)

    # Запись в первый файл
    with open(output_file1, 'w') as file1:
        file1.writelines(file1_lines)

    # Запись во второй файл
    with open(output_file2, 'w') as file2:
        file2.writelines(file2_lines)

    return len(file1_lines), len(file2_lines)

# Пути к файлам
input_file = 'PZ_14/ip_address.txt'
output_file1 = 'PZ_14/non_zero_octets.txt'
output_file2 = 'PZ_14/other_octets.txt'

# Выполнение функции
count1, count2 = split_ip_addresses(input_file, output_file1, output_file2)

print(f"Количество строк в первом файле: {count1}")
print(f"Количество строк во втором файле: {count2}")
