# Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
import my_func

def check_float(text):
    try:
        float_num = float(text)
        return print(f'{float_num} - это дробное число!')
    except(ValueError):
        print(f'"{text}" - это не дробное число!')
        return check_float(my_func.get_str('Введите строку заного: '))

check_float(my_func.get_str('Введите строку: '))