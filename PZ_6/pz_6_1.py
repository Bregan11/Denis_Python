# Даны целые числа N (>2), A и B. 
# Сформировать и вывести целочисленный список размера 10, 
# первый элемент которого равен A, 
# второй равен B, а каждый последующий элемент равен сумме всех предыдущих.

N = int(input("Введите целое число N (>2): "))
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

result_list = [A, B]
for i in range(2, 10):
    result_list.append(sum(result_list))

print("Сформированный список:", result_list)