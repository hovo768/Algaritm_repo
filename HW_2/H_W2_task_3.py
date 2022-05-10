'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''

user_num = int(input('Введите ваше число: '))
reversed_num = 0
i = 0
while user_num > 0:
    last_num = user_num % 10
    user_num = user_num // 10
    reversed_num = reversed_num * 10
    reversed_num = reversed_num + last_num

print(reversed_num)