'''Во втором массиве сохранить индексы четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.'''
import random
MAX_NUM = 100
MIN_NUM = 1
SIZE = 8
result = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(result)
result_2_revenge = []
for i, item in enumerate(result):
    if item % 2 == 0:
        result_2_revenge.append(i)

print(f'{result_2_revenge}')