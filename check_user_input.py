# Данный модуль проверяет ввод пользователя.

import re
from color_out import out_red as red
from color_out import out_white as white
from color_out import out_yellow as yellow
from logger_user_action import logger_action as log


def check_complex(x):
    reg = re.search(r"^\D?\d{1,}\D\d*\D{1}$", x)
    return True if reg else False


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
                elif check_complex(user_input.replace(' ', '')):
                    ind_char = '/*+-%'
                    char_ = None
                    imaginary = None
                    sign = 1
                    user_input_co = user_input
                    for i in range(len(user_input_co)):
                        if user_input_co[0] == '-':
                            sign = -1
                            # continue
                        if user_input_co[i].isalpha():
                            imaginary = user_input_co[i]
                        for j in ind_char:
                            if  user_input_co[i] == j:
                                char_ = user_input_co[i]
                    if char_ == '+' or char_ == '-':
                        # user_input_co = user_input_co.replace(char_, f' {char_} ')
                        log(f'ввел комплексное число: {user_input}.')
                        if sign == -1:
                            user_input_co = user_input_co[1:]
                        user_input_co = user_input_co.split(char_)
                        user_input_co[0] = user_input_co[0].replace(' ', '')
                        user_input_co[1] = user_input_co[1].replace(f'{imaginary}', '', 1).replace(' ', '')
                        if not user_input_co[1] or user_input_co[1].isalpha():
                            user_input_co[1] = '1'
                        if user_input_co[0].isdigit() and user_input_co[1].isdigit  () :
                            user_input_co = list(map(int, user_input_co))
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