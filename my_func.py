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