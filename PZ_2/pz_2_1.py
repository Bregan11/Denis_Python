def centimeters_to_meters(length_cm):
    """
    Преобразует длину из сантиметров в полные метры.

    Args:
    length_cm (int): Длина в сантиметрах.

    Returns:
    int: Количество полных метров.
    """
    return length_cm // 100

def main():
    try:
        # Запрашиваем у пользователя ввод расстояния в сантиметрах
        length_cm = int(input("Введите расстояние в сантиметрах: "))
        
        # Проверяем, что введенное значение неотрицательное
        if length_cm < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        
        # Вычисляем количество полных метров
        meters = centimeters_to_meters(length_cm)
        
        # Выводим результат
        print(f"В {length_cm} см содержится {meters} полных метров.")
    
    except ValueError as ve:
        # Обрабатываем ошибку ввода
        print(f"Ошибка: {ve}. Пожалуйста, введите корректное целое число.")

if __name__ == "__main__":
    main()