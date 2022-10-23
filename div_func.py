# Модуль производит деление.

from check_user_input import user_input_check as UI_check
from logger_user_action import logger_action as log
from color_out import out_white as white
from color_out import out_red as red
from color_out import out_green as green



def division_func(x):
    if x == 0:
        nums1 = UI_check(2, 0)
        nums2 = UI_check(2, nums1)
    else:
        nums1 = UI_check(2, 0, x)
        nums2 = UI_check(2, nums1)
    log(f'Ввел 1 число: {nums1}, второе: {nums2}.')
    if nums2 == 0:
        red('\nМатематическая ошибка, на "0" делить нельзя!')
        white('')
        log('пытается делить на "0", программа запросила повторный ввод.')
        nums2 = UI_check(2, nums1)
        if nums2 == 0:
            log('повторно  пытается делить на "0". программа отправила юзера в главное меню. вернув результат "0"')
            red('\nВыберите другую операцию. результат = 0')
            white('')
            return 0
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 / nums2, 3)
        log(f'получил результат: {result} .')
        green(f'\n({nums1}) / ({nums2}) = {result} ')
        white('')
        return result
    else:
        result = []
        nnums1 = []
        nnums2 = []
        if isinstance(nums1, int|float) and isinstance(nums2, tuple):
            if nums1 == 0:
                result = 0
                log(f'получил результат: {result} .')
                green(f'\n({nums1[3]}) / ({nums2[3]}) = {result} ')
                white('')
                return result
            else:
                nnums1, nums1 = nums1, nnums1
                nums1.append(nnums1)
                nums1.append(0)
                nums1.append(nums2[2])
                nums1.append(str(nnums1))
        elif isinstance(nums2, int|float) and isinstance(nums1, tuple):
            if nums2 == 0:
                red('\nМатематическая ошибка, на "0" делить нельзя!')
                white('')
                log('пытается делить на "0", программа запросила повторный ввод.')
                nums2 = UI_check(2, nums1)
                if nums2 == 0:
                    log('повторно  пытается делить на "0". программа отправила юзера в главное меню. вернув результат "0"')
                    red('\nВыберите другую операцию. результат = 0')
                    white('')
                    return 0
            else:
                nnums2, nums2 = nums2, nnums2
                nums2.append(nnums2)
                nums2.append(0)
                nums2.append(nums1[2])
                nums2.append(str(nnums2))
        a = (nums1[0] * nums2[0] + nums1[1] * nums2[1])\
            /(nums2[0] ** 2 + nums2[1] ** 2)
        if a != 0:
            result.append(str(round(a, 3)))
        b = (nums2[0] * nums1[1] - nums1[0] * nums2[1])\
            /(nums2[0] ** 2 + nums2[1] **  2)
        if b != 0:
            if b > 0:
                if a != 0:
                    result.append('+')
            elif b < 0:
                result.append('-')
            if b == 1 or b == -1:
                result.append(nums2[2])
            else:
                result.append(str(round(abs(b), 3)) + nums2[2])
        if len(result) == 0:
            result = 0
        else:
            result = ' '.join(result)
        log(f'получил результат: {result} .')
        green(f'\n({nums1[3]}) / ({nums2[3]}) = {result} ')
        white('')
        return result
