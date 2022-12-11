# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

a = randint(0, 20) # задаём количество элементов списка
list_x = list()

for i in range(a):
    x = randint(0, 10)
    list_x.append(x)

sum_m = 0

for i in range(1, len(list_x), 2):
        sum_m += list_x[i]

print(list_x)   
print(f"сумма элементов на нечётных позициях: {sum_m}")