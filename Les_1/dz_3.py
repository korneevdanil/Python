# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('Введите любое число x, кроме 0:'))
y = int(input('Введите любое число y, кроме 0:'))


if x == 0 and y == 0:
    print("Сказано же было, любое кроме 0, ПОКА!")
elif x > 0 and y > 0:
    print("Ваша точка в плоскости 1!")
elif x > 0 and y < 0:
    print("Ваша точка в плоскости 2!")
elif x < 0 and y < 0:
    print("Ваша точка в плоскости 3!")
elif x < 0 and y > 0:
    print("Ваша точка в плоскости 4!")