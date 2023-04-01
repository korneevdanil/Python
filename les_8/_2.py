with open('newfile.txt', 'w', encoding='utf-8') as g:
    d = 123
    print('1 / {} = {}'.format(d, 1 / d), file = g)