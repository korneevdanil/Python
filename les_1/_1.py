# Для простоты проверки работы используем randint

from random import randint

a = randint(100, 999)

# a = int(input("Введите целое трёхзначное число: "))

if a >= 100 and a < 1000:
    a = str(a)
    x = 0
    for i in a:
        x += int(i)
    print(f'Сумма цифр введённого числа:  {x}')
else:
    print("Вы ввели число не соответствующее условиям! ")




