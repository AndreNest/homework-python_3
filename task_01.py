# 3.10 Вводим с клавиатуры десятичное число.
# Необходимо перевести его в шестнадцатиричную систему счисления.
import my_func
def converte10_16(num):
    start_num = num
    converte_16 = []
    while start_num > 0:
        x = start_num % 16
        if x < 10:
            converte_16.append(str(x))
        if x == 15:
            converte_16.append('F')
        elif x == 14:
            converte_16.append('E')
        elif x == 13:
            converte_16.append('D')
        elif x == 12:
            converte_16.append('C')
        elif x == 11:
            converte_16.append('B')
        elif x == 10:
            converte_16.append('A')
        start_num //= 16


    converte_16.reverse()
    new_list = ''.join(converte_16)
    print(f'Число в 16 ричной С.С.  = {new_list}')


converte10_16(my_func.get_int('Введите число: '))
