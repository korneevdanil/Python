

def rek(a, b):
    if b == 0:
        return 1
    return a * rek(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

print(rek(a, b))
