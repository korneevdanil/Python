import time

# засекаем время начала работы скрипта 
# или куска кода

t_start = time.perf_counter()

# здесь код, время/производительность 
# которого необходимо замерить
with open('newfile.txt', 'w', encoding='utf-8') as g:
    d = 123
    print('1 / {} = {}'.format(d, 1 / d), file = g)

time.sleep(1)

# засекаем время окончания работы скрипта
# или куска кода

all_time = time.perf_counter() - t_start
print(round(all_time, 2))
# 1.0023632319971512