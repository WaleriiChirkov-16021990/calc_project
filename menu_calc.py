# Данный блок отображает базовое меню калькулятора.
# Блок не прекращает работу пока пользователь не захочет закрыть его.
# Меню реагирует на ввод пользователя в комнадную строку и видоизменяется\
#  в соответствии с выбором пользователя.


from curses.ascii import isalpha, isdigit


def user_input_check(f: function, x):
    while True:
        if x == 0:
            user_input = input('Введите первое число: ')
        else:
            user_input = input('Введите второе число: ')
        try:
            if f == menu_calc:
                user_input = int(user_input)
                if 1 <= user_input <= 5:
                    break
                else:
                    raise ValueError
            if f == sum_func  :
                if user_input.isdigit() and not isinstance(x, tuple):
                    user_input = int(user_input)
                    break
                if user_input.replace('.', 1).replace(',', 1).isdigit() \
                                            and not isinstance(x, tuple):
                    user_input = float(user_input)
                    break
                elif user_input.count('i') or user_input.count('j'):
                    ind_char = '/*+-%'
                    char_ = None
                    imaginary = None
                    sign = 1
                    user_input = user_input.replace(' ', '')
                    for i in range(len(user_input)):
                        if user_input[0] == '-':
                            sign = -1
                        if user_input[i].isalpha():
                            imaginary = i
                        for j in ind_char:
                            if  i == j:
                                char_ = i
                    user_input = user_input.split(char_)
                    user_input[0] = user_input[0].replace(' ', '')
                    user_input[1] = user_input[1].replace(imaginary, '', 1)\
                                    .replace(' ', '')
                    if user_input[0].isdigit() and user_input[1].isdigit() :
                        user_input = list(map(int, user_input))
                        if char_ == '-':
                            user_input[1] = - user_input[1]
                        if sign == -1:
                            user_input[0] == - user_input[0]
                        return user_input[0], user_input[1], imaginary
                    else:
                        raise ValueErrornums
                else:
                    raise ValueError
        except ValueError:
            if f == menu_calc:
                print('Выберете действие из предложенного списка.')
            continue
        except ValueErrornums:
            if x != 0:
                print('Введите второе число, подобное первому')
            else:
                print('Введите комплексное чмсло в виде "a + bi" .')
            continue
    return user_input


def sum_func():
    nums1 = user_input_check(sum_func, 0)
    nums2 = user_input_check(sum_func, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        return nums1 + nums2

def subtraction_func():
    result = None
    nums1 = user_input_check(sum_func, 0)
    nums2 = user_input_check(sum_func, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = nums2 - nums1
        return result
    else:
        result = []
        result.append(nums1[0] - nums2[0])
        result.append(str(nums1[1] - nums2[1]) + str(num2[2]) )
        print(' '.join(result))
        return ' '.join(result)


def multiplication_func():
    nums1 = user_input_check(sum_func, 0)
    nums2 = user_input_check(sum_func, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        return nums1 + nums2


def division_func():
    nums1 = user_input_check(sum_func, 0)
    nums2 = user_input_check(sum_func, nums1)
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        return nums1 + nums2



def menu_calc():
    print('Привед вам калькулятор.')
    print('Для дальнейшей работы введите цифру, которая соответствует пункту меню.')
    print('1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Выход')
    result = []
    user_input = user_input(menu_calc)
    if user_input == 1:
        sum_func()
    elif user_input == 2:
        subtraction_func()
    elif user_input == 3:
        multiplication_func()
    elif user_input == 4:
        division_func()
    else:








menu_calc()
