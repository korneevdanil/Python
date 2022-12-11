# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint

n = int(input('Введите число N (количество элеметов списка): '))
list_x = list()

for i in range(n):
    x = randint(0, 10)
    list_x.append(x)

print(f"исходный список:\n {list_x}")


for i in range(len(list_x)):
    x = randint(0, 6)
    a = list_x.pop()
    list_x.insert(x, a)

print(f"перемещанный список:\n {list_x}")


