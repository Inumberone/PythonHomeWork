# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

numb=float (input('Введи вещественное число: '))
str_numb=str(numb)
str_numb = str_numb.replace('.', '')
list_str = list(str_numb)
list_numb = map(int, list_str)
sum_numb = sum(list_numb)
print(sum_numb)


# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
print('введи список чисел')
x=int (input('Введи число: '))
x1= (1 + 1/x)**x
y=int (input('Введи число: '))
y1= (1 + 1/y)**y
z=int (input('Введи число: '))
z1= (1 + 1/z)**z
my_list = f'[{x1}],[{y1}],[{z1}]'
print(f'список n: {my_list}')
sum_lst = float ((1 + 1/x)**x + (1 + 1/y)**y + (1 + 1/z)**z)
print (f'сумма чисел списка n = {sum_lst}')

# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
from random import randint as rnd
import random

size=int(input('Введите размер списка: '))
rnd_list = []
for i in range(size):
    rnd_list.append(rnd(0,100))

print (f'Оргинальный список - {rnd_list}')
sample_list=random.sample(rnd_list, len (rnd_list))
print (f'Перемешанный список - {sample_list}')


