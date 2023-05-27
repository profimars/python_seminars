# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число N: '))
k = 0
s = 0
while k < N:
    s = 2 ** k
    k = k + 1
    if s >= N:
        break
    print(s, end='  ')
print()
f = 0
for i in range(N):
    f = 2 ** i
    if f >= N:
        break
    print(f, end='  ')

