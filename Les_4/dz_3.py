from random import randint

lst_a = list()

for i in range(10): # Формируем последовательность чисел
    a = randint(1, 10)
    lst_a.append(a)

lst_b = lst_a.copy()
lst_x = list()

for i in range(len(lst_b)):
    x = lst_b.pop(0)
    if x not in lst_b:
        lst_x.append(x)


print(f"Заданный список: {lst_a}")
print(f"Cписок неповторяющихся элементов: {lst_x}")
