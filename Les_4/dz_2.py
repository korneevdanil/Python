# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное число: "))
i = 2 # первй простой множитель
lst = []
n = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"{lst} - Это список простых множителей числа: {n}")