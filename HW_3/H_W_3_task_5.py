import random
SIZE = 10
MAX_NUM = - 1
MIN_NUM = - 1000
result = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(result)

inf_num = float('-inf')
num = float('-inf')
for i, item in enumerate(result):
    if 0 > item > num:
        num = item
        indx = i

if num != inf_num:
    print(f'Макс. отрицательное число это {num} '
          f' которая находится в ячейке {indx}')