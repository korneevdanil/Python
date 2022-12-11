# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]


def r_lst(lst):
    if len(lst) % 2 != 0:
        l = len(lst) // 2 + 1
    else:
        l = len(lst) // 2
    r_list = list()
    for i in range(l):
        x = lst[i] * lst[len(lst) - i - 1]
        r_list.append(x)
    return r_list

lst = [2, 3, 4, 5, 6]
result = r_lst(lst)

print(result)

