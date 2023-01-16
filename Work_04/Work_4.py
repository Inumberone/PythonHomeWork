#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

size1 = int(input('Введите максимальную степень: '))
size2 = int(input('Введите максимальную степень: '))

def create_eq (size):
    koef = {}
    for i in range(size+1):
        koef[i]=random.randint(0,5)
 


    equation =''
    for i in range(size, -1, -1 ):
        if koef[i] != 0:
            if koef[i] == 1:
                if i == 1:
                    equation += f'x + '
                elif i == 0:
                    equation += f'1 '
                else:
                    equation += f'x**{i} + '
            
            else:
                if i == 1:
                    equation += f'{koef[i]}*x + '
                elif i == 0:
                    equation += f'{koef[i]} '
                else:
                    equation += f'{koef[i]}*x**{i} + '

    return equation + " = 0"
            
print(create_eq(size1))
with open('size1.txt', 'w') as data:
    data.writelines(create_eq(size1))
    

print(create_eq(size2))
with open('size2.txt', 'w') as data:
    data.writelines(create_eq(size1))

with open('size1.txt', 'r', encoding = 'UTF-8') as data:
    string = data.readline()
print(string)


with open('size2.txt', 'r', encoding = 'UTF-8') as data:
    string = data.readline()
print(string)

