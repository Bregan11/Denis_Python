# Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.

import random

def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

def task2_variant6(rows, cols):
    matrix = generate_matrix(rows, cols, 1, 20)
    print_matrix(matrix, "Исходная матрица для Задания 2")
    new_matrix = [[(0 if x > 10 else x) for x in row] for row in matrix]
    return new_matrix

if __name__ == "__main__":
    rows_task2 = 3
    cols_task2 = 5
    result_matrix_task2 = task2_variant6(rows_task2, cols_task2)
    print_matrix(result_matrix_task2, "Матрица после выполнения Задания 2 (элементы > 10 заменены на 0)")
