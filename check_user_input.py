# Данный модуль проверяет ввод пользователя.

import re
from color_out import out_red as red
from color_out import out_white as white
from color_out import out_yellow as yellow
from logger_user_action import logger_action as log


def check_complex(x):
    reg = re.search(r"^\D?\d{1,}\D\d*\D{1}$", x)
    return True if reg else False


def check_2_complex(x):
    math = re.search(r'^\D?\d*\D{1}$', x)
    return True if math else False


def check_3_complex(x):
    math = re.search(r'^[+-]?\d*?[.]?\d{0,4}[+-]?\d*?[.]\d{0,4}\D{1}?$', x)
    return True if math else False


def sub(x: str):
    y = None
    if x[0] == '-' or x[0] == '+':
        y = re.sub(r'^\D?\d*\D{1}$', f'0{x}', x)
    if x[0].isdigit():
        y = re.sub('\d*\D{1}', f'0+{x}', x)
    if x[0].isalpha():
        y = re.sub('\D{1}', f'0+1{x}', x)
    return y if y else False


def user_input_check(f: int, x, num1 = None):
    while True:
        if x == 0 and f == 2 and num1:
            user_input = str(num1).strip()
            yellow(f'Первое число = {user_input}')
            white('')
        elif x == 0 and f == 2:
            user_input = input('Введите первое число: ').strip()
        elif f == 2 and x != 0:
            user_input = input('Введите второе число: ').strip()
        elif f == 1:
            user_input = input('Выберите операцию: ').strip()
        try:
            if f == 1 :
                user_input = int(user_input)
                if 1 <= user_input <= 5:
                    return user_input
                else:
                    raise ValueError
            elif f == 2:
                if user_input.replace('-', '').isdigit():
                    return int(user_input)
                elif user_input.replace('-', '').replace('.', '1').replace(',', '1').isdigit():
                        return float(user_input)
                elif check_complex(user_input.replace(' ', '')) \
                    or check_2_complex(user_input.replace(' ', ''))\
                        or check_3_complex(user_input.replace(' ', '')):
                    float_ = check_3_complex(user_input.replace(' ', ''))
                    ind_char = '/*+-%'
                    char_ = None
                    imaginary = None
                    sign = 1
                    if check_2_complex(user_input):
                        user_input_co = sub(user_input.replace(' ', ''))
                    else:
                        user_input_co = user_input.replace(' ', '')
                    for i in range(len(user_input_co)):
                        if user_input_co[0] == '-':
                            sign = -1
                        if user_input_co[i].isalpha():
                            imaginary = user_input_co[i]
                        for j in ind_char:
                            if  user_input_co[i] == j:
                                char_ = user_input_co[i]
                    if char_ == '+' or char_ == '-':
                        if sign == -1:
                            user_input_co = user_input_co[1:]
                        user_input_co = user_input_co.split(char_)
                        user_input_co[1] = user_input_co[1].replace(f'{imaginary}', '', 1)
                        if not user_input_co[1] or user_input_co[1].isalpha():
                            user_input_co[1] = '1'
                        if user_input_co[0].isdigit() \
                            and user_input_co[1].isdigit() :
                            user_input_co = list(map(int, user_input_co))
                            if char_ == '-':
                                user_input_co[1] = - user_input_co[1]
                            if sign == -1:
                                return -1 * user_input_co[0], user_input_co[1], imaginary,   user_input
                            return user_input_co[0], user_input_co[1], imaginary,   user_input
                        elif float_:
                            user_input_co = list(map(float, user_input_co))
                            if char_ == '-':
                                user_input_co[1] = - user_input_co[1]
                            if sign == -1:
                                return -1 * user_input_co[0], user_input_co[1], imaginary,   user_input
                            return user_input_co[0], user_input_co[1], imaginary,   user_input
                        else:
                            raise TypeError
                    else:
                        raise TypeError
                else:
                    raise ValueError
        except ValueError:
            if f == 1:
                log('выбрал неизвестное действие.')
                red('Выберете действие из предложенного списка.')
                white('')
            elif f == 2:
                log('ввёл неизвестное число.')
                red('Вы ввели неизвестное число.')
                white('')
            continue
        except TypeError:
            log('пытался ввести комплексное число но что то напутал на клавиатуре.')
            red('Введите комплексное число в виде "a +(-) bi" .')
            white('')
            continue
