# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и
# последней буквой "о".
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
import my_func

def check_str(text):
    check_o = 0
    for el in text:
        if el == 'О' or el == 'о':
            check_o +=1
    if check_o < 2:
        print(f'Буква "О", встречается {check_o} раз. \nЭто не подходит под условия задачи.')
    else:
        start_max = text.find('О')
        start_min = text.find('о')
        finish_max= text.rfind('О')
        finish_min= text.rfind('о')
        start = 0
        finish = 0
        if start_max == -1:
            start = start_min
        elif start_min == -1:
            start = start_max
        elif start_min > start_max:
            start = start_max
        elif start_max > start_min:
            start = start_min
        if finish_min == -1:
            finish = finish_max
        elif finish_max == -1:
            finish = finish_min
        elif finish_max > finish_min:
            finish = finish_max
        elif finish_min > finish_max:
            finish = finish_min
        print(f'{text[:start]}{text[finish:start:-1]}{text[finish:]}')




        print(f'{start_min} - start min, {start_max} - start max\n {finish_min} - finish min, {finish_max} - finish max\n {start} - start, {finish} - finish')

check_str(my_func.get_str('Введите строку!'))