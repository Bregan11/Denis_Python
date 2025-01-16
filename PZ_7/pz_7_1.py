# Дан символ C, изображающий цифру или букву (латинскую или русскую). Если C 
# изображает цифру, то вывести строку «digit», если латинскую букву — вывести 
# строку «lat», если русскую — вывести строку «rus». 

def check_char_type(char):
    if char.isdigit():
        return "digit"
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        return "lat"
    elif 'а' <= char <= 'я' or 'А' <= char <= 'Я':
        return "rus"
    else:
        return "unknown"

if __name__ == '__main__':
    try:
        char_input = input("Введите символ: ")
        if len(char_input) != 1:
             raise ValueError("Необходимо ввести один символ")
        result = check_char_type(char_input)
        print(result)

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")