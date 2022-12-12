# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_encod.txt', 'w') as data:
    data.write('SSSSffffffffffTTTT')

with open('file_encod.txt', 'r') as data:
    string = data.readline()

def rle_encod (decod_string):
    encod_string = ''
    count  = 1
    num_list = decod_string[0]
    for i in range(1, len(decod_string)):
        if decod_string[i] == num_list:
            count += 1
        else:
            encod_string = encod_string + str(count) + num_list
            num_list = decod_string[i]
            count  = 1
            encod_string = encod_string + str(count) + num_list
    return encod_string

def rle_decod(encod_string):
    decod_string = ''
    num_list_col = ''
    for i in range(len(encod_string)):
        if encod_string[i].isdigit():
            num_list_col += encod_string[i]
        else:
            decod_string += encod_string[i] * int(num_list_col)
        num_list_col = ''
    print(decod_string)

    return decod_string


with open('file_encod.txt', 'r') as file:
    decod_string = file.read()

with open('file_decod.txt', 'w') as file:
    encod_string = rle_encod(decod_string)
    file.write(encod_string)

print(f'Полная строка: {decod_string}')
print(f'Сжатая строка: {rle_encod(decod_string)}')