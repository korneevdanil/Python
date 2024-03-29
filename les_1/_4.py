# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите число долек шоколадки по вертикали: "))
m = int(input("Введите число долек шоколадки по горизонтали: "))
k = int(input("Введите число долек, которое вы хотите отломить: "))

if k < n * m:
    if k % n == 0 or k % m == 0:
        print(f'{k} долек можно отломить!')
    else:
        print(f'{k} долек нельзя отломить!')
else:
    print(f'{k} долек нельзя отломить!')