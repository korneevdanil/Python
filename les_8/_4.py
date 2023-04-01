
import time
# Без использования менеджера контекста

start = time.perf_counter()

with open('newfile1.txt', 'w', encoding='utf-8') as g:
    d = 100
    for i in range(1, 9990000):
        a = i * 100000
        g.write(str(a) + '\n')

executionl_time = time.perf_counter() - start
print(float(executionl_time))


with open('newfile1.txt', 'w', encoding='utf-8') as g:
    g.write(str(999))

executionl_time = time.perf_counter() - start
print(float(executionl_time))