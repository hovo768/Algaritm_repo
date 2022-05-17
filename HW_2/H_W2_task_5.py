'''
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме:
по десять пар "код-символ" в каждой строке.
'''
f_num = 32
l_num = 127
step_num = 10
steps = 0

while f_num <= l_num:
    steps+=1
    print(f'{f_num}--{chr(f_num)}\t\t', end=' ')
    if steps == step_num:
        steps = 0
        print('')
    f_num += 1



'''можете обяснить пожалуста, как тут нужно правильно сконаструировать рекурсию
'''
# def numer(a=32, b=127, step = 10, steps=0):
#     if a == b:
#         return f'{a} - {chr(a)}'
#     print(f'{a} - {chr(a)}\t', end='')
#     if steps == step:
#         numer(steps = 0)
#         print('')
#     else:
#         return numer(a+1, steps+1)
#
# print(numer())