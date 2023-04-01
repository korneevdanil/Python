with open('newfile1.txt', 'w', encoding='utf-8') as g:
    d = 100
    for i in range(1, 1000000):
        a = i * 100000
        g.write(str(a) + '\n')