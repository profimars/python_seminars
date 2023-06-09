# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input("Введите n: "))
m = int(input("Введите m: "))
list1 = []
for i in range(n):
    list1.append(int(input("Введите число первого листа : ")))
print(list1)
list2 = []
for i in range(m):
     list2.append(random.randint(0, 5))
print(list2)
list_result = []
for i in list1:
    for j in list2:
        if i == j:
            list_result.append(i)
print(set(list_result))

