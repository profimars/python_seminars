# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("Введите количество элементов в массиве N: "))
A = [int(i + 1) for i in range(N)]
A.append(3)
A.insert(0, 3)
A.insert(4, 3)
print(A)
X = int(input("Введите искомое число X: "))
K = 0
for i in A:
    if i == X:
        K = K + 1
print(f"Количество числа {X} в массиве {K} штук.")