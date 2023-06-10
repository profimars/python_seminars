# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random

n = int(input("Введите количество элементов массива n: "))
range_l = int(input("Введите левую границу диапазона range_l: "))
range_r = int(input("Введите правую границу диапазона range_r: "))

list = []
for i in range(n):
    e = random.randint(0, 9)
    list.append(e)
list.sort()
print(list)

list_index = []
for i in range(n):
    if list[i] >= range_l and list[i] <= range_r:
        list_index.append(i)
print(list_index)
