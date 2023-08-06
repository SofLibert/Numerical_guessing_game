from random import *

num = randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def proverka(s):
    while is_valid(s) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        s = input()
        is_valid(s)
    return int(s)

print('Введите число')
n = input()
n = proverka(n)

while n != num:
    if n < num:
        print('Ваше число меньше загаданного, попробуйте еще разок :(')
    elif n > num:
        print('Ваше число больше загаданного, попробуйте еще разок :(')
    n = input()
    n = proverka(n)

print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')