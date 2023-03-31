
from random import randint

x = randint(1, 10)
y = randint(1, 10)

print(x, y)

sum = x + y
prod = x * y

for q in range(sum):
    for w in range(prod):
        if q + w == sum and q * w == prod:
            break
    if q + w == sum and q * w == prod:
        print(f'Загаданные числа {q} и {w}')
        break