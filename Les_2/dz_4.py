# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры.

from random import randint

n = int(input('Введите число N: '))
list_x = list()
a = int(input('Введите позицию a (обозначать числом) до ' + str(n-1) + ': '))
b = int(input('Введите позицию b (обозначать числом) до ' + str(n-1) + ': '))

for i in range(n):
    x = randint(-n, n)
    list_x.append(x)

result = a * b

print(result)


