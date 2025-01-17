# Дана строка-предложение на русском языке. Зашифровать ее, выполнив 
# циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при 
# этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т. 
# д.). Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки 
# препинания и пробелы не изменять.

def encrypt_sentence(sentence):
    encrypted_sentence = ""
    for char in sentence:
        if 'а' <= char <= 'я':
            start = ord('а')
            encrypted_char = chr((ord(char) - start + 1) % 32 + start)
        elif 'А' <= char <= 'Я':
             start = ord('А')
             encrypted_char = chr((ord(char) - start + 1) % 32 + start)
        else:
            encrypted_char = char
        encrypted_sentence += encrypted_char
    return encrypted_sentence

if __name__ == '__main__':
    try:
        sentence = input("Введите предложение на русском языке: ")
        encrypted = encrypt_sentence(sentence)
        print("Исходное предложение:", sentence)
        print("Зашифрованное предложение:", encrypted)
    except Exception as e:
        print(f"Произошла ошибка: {e}")