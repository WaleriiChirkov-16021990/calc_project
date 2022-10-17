# Данный блок отображает базовое меню калькулятора.
# Блок не прекращает работу пока пользователь не захочет закрыть его.
# Меню реагирует на ввод пользователя в комнадную строку и видоизменяется\
#  в соответствии с выбором пользователя.


import re


def check_complex(x):
    reg = re.search(r"^[a-zA-Z]+$",r'x')
    if reg:
        reg = True
    else:
        reg = False
    return reg


def user_input_check(f: int, x):
    while True:
        if x == 0 and f == 2:
            user_input = input('Введите первое число: ')
        elif f == 2 and x != 0:
            user_input = input('Введите второе число: ')
        elif f == 1:
            user_input = input('Выберите операцию: ')
        try:
            if f == 1 :
                user_input = int(user_input)
                if 1 <= user_input <= 5:
                    break
                else:
                    raise ValueError
            if f == 2:
                if user_input.isdigit() and not isinstance(x, tuple):
                    user_input = int(user_input)
                    return user_input
                elif user_input.replace('.', '1').replace(',', '1').isdigit() and not isinstance(x, tuple):
                    user_input = float(user_input)
                    return user_input
                elif check_complex(user_input):
                    ind_char = '/*+-%'
                    char_ = None
                    imaginary = None
                    sign = 1
                    user_input_co = user_input.replace(' ', '')
                    for i in range(len(user_input_co)):
                        if user_input_co[0] == '-':
                            sign = -1
                        if user_input_co[i].isalpha():
                            imaginary = user_input_co[i]
                        for j in ind_char:
                            if  user_input_co[i] == j:
                                char_ = user_input_co[i]
                    user_input_co = user_input_co.split(char_)
                    user_input_co[0] = user_input_co[0].replace(' ', '').replace('-', '')
                    user_input_co[1] = user_input_co[1].replace(f'{imaginary}', '', 1)\
                        .replace(' ', '')
                    if user_input_co[0].isdigit() and user_input_co[1].isdigit() :
                        user_input_co = list(map(int, user_input_co))
                        if char_ == '-':
                            user_input_co[1] = - user_input_co[1]
                        if sign == -1:
                            user_input_co[0] == - user_input_co[0]
                        return user_input_co[0], user_input_co[1], imaginary, user_input
                    else:
                        raise TypeError
                else:
                    raise ValueError
        except ValueError:
            if f == menu_calc:
                print('Выберете действие из предложенного списка.')
            continue
        except TypeError:
            if x != 0:
                print('Введите второе число, подобное первому')
            else:
                print('Введите комплексное число в виде "a + bi" .')
            continue
    return user_input


def sum_func(x):
    if x == 0:
        nums1 = user_input_check(2, 0)
        nums2 = user_input_check(2, nums1)
    else:
        nums1 = x
        nums2 = user_input_check(2, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 + nums2, 3)
        print(f'{nums1} + {nums2} = {result} ')
        return result
    else:
        result = []
        result.append(str(nums1[0] + nums2[0]))
        if nums1[1] + nums2[1] > 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(abs((nums1[1] + nums2[1]))) + nums2[2] )
        result = ' '.join(result)
        print(f'{nums1[3]} + {nums2[3]} = {result} ')
        return result


def subtraction_func(x):
    if x == 0:
        nums1 = user_input_check(2, 0)
        nums2 = user_input_check(2, nums1)
    else:
        nums1 = x
        nums2 = user_input_check(2, nums1)
    result = None
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 - nums2, 3)
        print(f'{nums1} - {nums2} = {result} ')
        return result
    else:
        result = []
        result.append(str(nums1[0] - nums2[0]))
        if nums1[1] - nums2[1] > 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(abs(nums1[1] - nums2[1])) + nums2[2])
        result = ' '.join(result)
        print(f'{nums1[3]} {nums2[3]} = {result} ')
        return result


def multiplication_func(x):
    if x == 0:
        nums1 = user_input_check(2, 0)
        nums2 = user_input_check(2, nums1)
    else:
        nums1 = x
        nums2 = user_input_check(2, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 * nums2, 3)
        print(f'{nums1} * {nums2} = {result} ')
        return result
    else:
        result = []
        result.append(str(nums1[0] * nums2[0] - nums1[1] * nums2[1]))
        if nums1[0] * nums2[1] + nums1[1] * nums2[0] > 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(abs(nums1[0] * nums2[1] + nums1[1] * nums2[0])) + nums2[2])
        result = ' '.join(result)
        print(f'{nums1[3]} * {nums2[3]} = {result} ')
        return result


def division_func(x):
    if x == 0:
        nums1 = user_input_check(2, 0)
        nums2 = user_input_check(2, nums1)
    else:
        nums1 = x
        nums2 = user_input_check(2, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 / nums2, 3)
        print(f'{nums1} / {nums2} = {result} ')
        return result
    else:
        result = []
        result.append(str(round((nums1[0] * nums2[0] + nums1[0] * nums2[1])/(nums2[0] ** 2 + nums2[1] ** 2), 3)))
        if (nums2[0] * nums1[1] - nums1[0] * nums2[1])/(nums2[0] ** 2 + nums2[1] ** 2) > 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(round(abs((nums2[0] * nums1[1] - nums1[0] * nums2[1])/(nums2[0] ** 2 + nums2[1] ** 2))), 3) + nums2[2])
        result = ' '.join(result)
        print(f'{nums1[3]} / {nums2[3]} = {result} ')
        return result


def menu_calc():
    print('Привед вам калькулятор.')
    user_input = None
    result = []
    while True:
        print('Для дальнейшей работы введите цифру, которая соответствует пункту меню.')
        print('1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Выход')
        user_input = user_input_check(1, 1)
        if user_input == 1:
            if len(result) > 0:
                print('')
                inp = int(input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: '))
                if inp == 1:
                    result.append(sum_func(result[-1]))
                else:
                    result.append(sum_func(0))
            else:
                result.append(sum_func(0))
            continue
        elif user_input == 2:
            if len(result) > 0:
                print('')
                inp = int(input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: '))
                if inp == 1:
                    result.append(subtraction_func(result[-1]))
                else:
                    result.append(subtraction_func(0))
            else:
                result.append(subtraction_func(0))
            continue
        elif user_input == 3:
            if len(result) > 0:
                print('')
                inp = int(input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: '))
                if inp == 1:
                    result.append(multiplication_func(result[-1]))
                else:
                    result.append(multiplication_func(0))
            else:
                result.append(multiplication_func(0))
            continue
        elif user_input == 4:
            if len(result) > 0:
                print('')
                inp = int(input('Использовать предыдущий результат вычисления?\nесли да введите 1, нет - введите 2: '))
                if inp == 1:
                    result.append(division_func(result[-1]))
                else:
                    result.append(division_func(0))
            else:
                result.append(division_func(0))
            continue
        elif user_input == 5:
            break


menu_calc()
