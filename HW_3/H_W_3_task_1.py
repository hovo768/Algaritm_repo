#sum, max, min нельзя !!!
'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

SUM_MIN = 2
SUM_MAX = 99
SUM_DICT_1 = 2
SUM_DICT_2 = 9
result = {key : 0 for key in range(SUM_DICT_1, SUM_DICT_2 + 1)}

for i in range(SUM_MIN, SUM_MAX + 1):
    for r in range(SUM_DICT_1, SUM_DICT_2 + 1):
        if i % r == 0:
            result[r] += 1
print(result)

