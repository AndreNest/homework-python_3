def get_int(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число!')
        return get_int(input_string)
def get_float(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = float(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число!')
        return get_float(input_string)
def float_num_check(num):
    num_x = num - round(num)
    if num_x == 0:
        print('num')
        print(f"{int(num)} - число не дробное!")
    else:
        print(f"{num} - число дробное!")

float_num_check(get_int('Введите число: '))

def get_str(input_string):
    '''
    Проверка ввода на строку.
    '''
    try:
        text = str(input(input_string))
        return  text
    except(ValueError):
        print('Ошибка ввода! Введите число!')
        return get_str(input_string)