# Данный блок отображает базовое меню калькулятора.
# Блок не прекращает работу пока пользователь не захочет закрыть его.
# Меню реагирует на ввод пользователя в комнадную строку и видоизменяется\
#  в соответствии с выбором пользователя.


from curses.ascii import isalpha, isdigit


def user_input(f: function):
    while True:
        user_input = input('ввод пользователя: ')
        try:
            if f == menu_calc:
                user_input = int(user_input)
                if 1 <= user_input <= 5:
                    break
                else:
                    raise ValueError
            if f == sum_func:
                if user_input.isdigit():
                    user_input = int(user_input)
                    break
                elif user_input.replace('.', 1).replace(',', 1).isdigit():
                    user_input = float(user_input)
                    break
                elif user_input.count('i'):
                    ind_char = '/*+-%'
                    char_ = None
                    imaginary = None
                    for i in user_input:
                        if i.isalpha():
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
                        return user_input, imaginary
                    else:
                        raise ValueError
        except ValueError:
            if f == menu_calc:
                print('Выберете действие из предложенного списка.')
            continue
    return user_input


def sum_func():




def menu_calc():
    print('Привед вам калькулятор.')
    print('Для дальнейшей работы введите цифру, которая соответствует пункту меню.')
    print('1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Выход')
    user_input = user_input(menu_calc)
    if user_input == 1:

    elif user_input == 2:


    elif user_input == 3:


    elif user_input == 4:

    else:








menu_calc()
