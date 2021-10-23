import random
import datetime
import os

# набор символов
ARRAY_SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c',
                 'A', 'B', 'C',
                 '!', '@']

CONST_COUNT_SYMBOLS = 4

custom_count_symbols = int(input("Введите количество символов в пароле: "))

if custom_count_symbols > 0:
    count_symbols = custom_count_symbols
else:
    count_symbols = CONST_COUNT_SYMBOLS


count_var = len(ARRAY_SYMBOLS) ** count_symbols


# функция случайных символов
def random_symbols():
    return ARRAY_SYMBOLS[random.randint(0, len(ARRAY_SYMBOLS) - 1)]


#массив символов
password_array = [i for i in range(0, count_symbols)]

print(password_array)

print(f'Версия приложения 0.0.1')
print(f'Количество доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Количество возможных вариантов: {count_var}')


password = ''

for i in password_array:
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

text_datetime = f'{datetime.datetime.now()}'
symbol_replace = ['.', ':', '-', ' ']

file_name = ''
for s in text_datetime:
    is_write = True
    for sr in symbol_replace:
        if s == sr:
            file_name += '_'
            is_write = False
    if is_write:
        file_name += s

if not os.path.exists('password'):
    os.mkdir('password')

with open(f'password/{file_name}.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
