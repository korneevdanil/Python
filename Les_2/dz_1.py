# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


x = input("Введите члюбое число: ")    # вводим любое число

number = 0

for i in str(x):                      # если есть точка или запятая, их удаляем
    if i != '.' and i != ',':
        number += int(i)

print(number)
