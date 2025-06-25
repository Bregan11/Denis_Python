# В двумерном списке элементы первого столбца возвести в куб.

import random

def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

def task1_variant6(matrix):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        if len(new_matrix[i]) > 0:
            new_matrix[i][0] = new_matrix[i][0] ** 3
    return new_matrix

if __name__ == "__main__":
    rows_task1 = 3
    cols_task1 = 4
    matrix_task1 = generate_matrix(rows_task1, cols_task1, 1, 10)
    print_matrix(matrix_task1, "Исходная матрица для Задания 1")
    result_matrix_task1 = task1_variant6(matrix_task1)
    print_matrix(result_matrix_task1, "Матрица после выполнения Задания 1 (первый столбец в кубе)")
