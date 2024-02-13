from random import *

array = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if j >= i:
            array[i][j] = j - i + 1
for _ in array:
    print(_)
