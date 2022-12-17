from random import randint

lst_a = list()

for i in range(10): # Формируем последовательность чисел
    a = randint(1, 10)
    lst_a.append(a)

lst_x = list()

for i in range(len(lst_a)): #удаляем элемент из списка и проверяем, есть ли повторяющийся
    x = lst_a.count(lst_a[i])
    if x <= 1:
        lst_x.append(lst_a[i])


print(f"Заданный список: {lst_a}")
print(f"Cписок неповторяющихся элементов: {lst_x}")
