# Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
import my_func

def check_float(text):
    try:
        float_num = float(text)
        return print(f'{float_num} - это дробное число!')
    except(ValueError):
        print(f'"{text}" - это не дробное число!')
        return check_float(my_func.get_str('Введите строку заного: '))
def float_num_check(num):
    num_x = num - round(num)
    if num_x == 0:
        print('num')
        print(f"{int(num)} - число не дробное!")
    else:
        print(f"{num} - число дробное!")

float_num_check(my_func.get_float('Введите число: '))
check_float(my_func.get_str('Введите строку: '))

