from random import *

# Генерируем случайные числа и записываем их в файл f
with open('f.txt', 'w') as file_f:
    for _ in range(10):
        num = randint(1, 100)
        file_f.write(str(num) + '\n')

# Читаем файл f и записываем четные числа в файл g
with open('f.txt', 'r') as file_f, open('g.txt', 'w') as file_g:
    for line in file_f:
        num = int(line.strip())
        if num % 2 == 0:
            file_g.write(str(num) + '\n')
