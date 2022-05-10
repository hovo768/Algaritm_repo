'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

def number_form(number, even = 0, odd = 0):
    if number == 0:
        return f'четных чисел: {even}\n' \
               f'нечетных чисел: {odd}'
    if number % 2 == 0:
         even += 1
    else:
        odd += 1
    number = number // 10
    return number_form(number, even, odd)


num = int(input('Ввеидите НАТУРАЛЬНОЕ число: '))
result = number_form(num)
print(result)

