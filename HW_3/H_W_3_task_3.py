''''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''
import random
MAX_NUM = 100
MIN_NUM = 1
SIZE = 8
result =[random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(result)

small_num = 0
big_num = 0
for i in range(len(result)):
    if result[i] < result[small_num]:
        small_num = i
    elif result[i] > result[big_num]:
        big_num = i

result[small_num], result[big_num] = result[big_num], result[small_num]

print(result)