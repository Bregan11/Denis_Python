# Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

import os
import string

# Чтение файла
with open('PZ_11/text18-6.txt', 'r', encoding='utf-16') as f:
    text = f.read()

# Подсчет пробелов
space_count = text.count(' ')
print(f'Количество пробелов: {space_count}')

# Замена пунктуации и запись в новый файл
additional_punctuation = '«»'
translation_table = str.maketrans(string.punctuation + additional_punctuation, '!' * (len(string.punctuation) + len(additional_punctuation)))
new_text = text.translate(translation_table)

# Создаем директорию, если она не существует
os.makedirs('PZ_11', exist_ok=True)

# Записываем новый текст в файл
with open('PZ_11/new_text.txt', 'w', encoding='utf-16') as f:
    f.write(new_text)

