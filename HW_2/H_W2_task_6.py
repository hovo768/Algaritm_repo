'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
'''

import random
print(f'Добро пожаловать в игру отгадай число !!!\n'
      f'нужно Отгадать число от 0 до 100 за 10 попыток\n')
number = random.randint(0, 100)
count = 0
while True:
    count+=1
    user = int(input('Введите целое число от 0 до 100: '))
    if user == number:
        print('Вы выиграли !!!')
        break
    elif user < number:
        print('Ваше число меньше загаданного (')
    else:
        print('Ваше число больше загаданного (')

    if count == 10:
        print(f'Вы проиграли( \n'
              f'правильный ответ {number}')
        break