# Данный блок отображает базовое меню калькулятора.
# Блок не прекращает работу пока, пользователь не захочет закрыть его.
# UI реагирует на ввод пользователя в комнадную строку и видоизменяется\
# в соответствии с выбором пользователя.

from check_user_input import user_input_check as UI_check
from color_out import out_blue as blue
from color_out import out_white as white
from color_out import out_yellow as yellow
from sum_function import sum_func as sum_func
from sub_func import subtraction_func as sub_func
from mult_func import multiplication_func as mult_func
from div_func import division_func as div_func
from logger_user_action import logger_action as log


def menu_calc():
    blue('\nПеред вами калькулятор.')
    white('')
    log('запустил калькулятор.')
    user_input = None
    result = []
    while True:
        print('\nДля дальнейшей работы введите цифру, которая соответствует пункту меню.')
        print('1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Выход')
        user_input = UI_check(1, 1)
        if user_input == 1:
            log('выбрал операцию сложение.')
            if len(result) > 0:
                print('')
                inp = int(input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: '))
                if inp == 1:
                    log('использует предыдущий результат.')
                    result.append(sum_func(result[-1]))
                else:
                    log('вводит новые значения.')
                    result.append(sum_func(0))
            else:
                log('вводит новые значения.')
                result.append(sum_func(0))
            continue
        elif user_input == 2:
            log('выбрал операцию вычитание.')
            if len(result) > 0:
                print('')
                inp = input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: ')
                if inp == '1':
                    log('использует предыдущий результат.')
                    result.append(sub_func(result[-1]))
                else:
                    log('вводит новые значения.')
                    result.append(sub_func(0))
            else:
                log('вводит новые значения.')
                result.append(sub_func(0))
            continue
        elif user_input == 3:
            log('выбрал операцию умножение.')
            if len(result) > 0:
                print('')
                inp = input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: ')
                if inp == '1':
                    log('использует предыдущий результат.')
                    result.append(mult_func(result[-1]))
                else:
                    log('вводит новые значения.')
                    result.append(mult_func(0))
            else:
                log('вводит новые значения.')
                result.append(mult_func(0))
            continue
        elif user_input == 4:
            log('выбрал операцию деление.')
            if len(result) > 0:
                print('')
                inp = input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: ')
                if inp == '1':
                    log('использует предыдущий результат.')
                    result.append(div_func(result[-1]))
                else:
                    log('вводит новые значения.')
                    result.append(div_func(0))
            else:
                log('вводит новые значения.')
                result.append(div_func(0))
            continue
        elif user_input == 5:
            log(f'произвел {len(result)} расчётов.')
            log('завершил программу.')
            yellow('программа завершена')
            white('')
            break


menu_calc()
