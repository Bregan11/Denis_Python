# Даны температуры за месяц март. Необходимо найти количество положительных 
# и отрицательных значений температур в месяце, самую низкую и самую высокую 
# температуры, а также среднемесячное значение температуры.

import random

def main():
    # Генерация случайных температур для марта (31 день)
    temperatures = [random.randint(-20, 20) for _ in range(31)]

    # Подсчет положительных и отрицательных температур
    positive_count = sum(1 for temp in temperatures if temp > 0)
    negative_count = sum(1 for temp in temperatures if temp < 0)

    # Поиск минимальной и максимальной температур
    min_temp = min(temperatures)
    max_temp = max(temperatures)

    # Вычисление среднемесячной температуры
    average_temp = sum(temperatures) / len(temperatures)

    # Вывод результатов
    print("Сгенерированные температуры за март:")
    print(temperatures)
    print("Количество положительных температур:", positive_count)
    print("Количество отрицательных температур:", negative_count)
    print("Самая низкая температура:", min_temp)
    print("Самая высокая температура:", max_temp)
    print("Среднемесячная температура:", average_temp)

if __name__ == "__main__":
    main()
