# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

x = 10
lst = list()
new_lst = list()


for i in range(x):
    a = uniform(1, 11)
    lst.append(a)

for i in lst:
    if i % 1 != 0:
        new_lst.append(round(i % 1, 2))

result = max(new_lst) - min(new_lst)

print(result)