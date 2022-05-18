# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
import random
MAX_NUM = 100
MIN_NUM = 0
SIZE = 8
resul =[random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(resul)

small_num = 0
big_num = 0
medium_num = 0
for i in range(1, len(resul)):
    if resul[i] < resul[small_num]:
        small_num = i
    elif resul[i] > resul[big_num]:
        big_num = i

if small_num > big_num:
    small_num, big_num = big_num, small_num


for i in range(small_num + 1, big_num):
    medium_num += resul[i]
print(medium_num)
