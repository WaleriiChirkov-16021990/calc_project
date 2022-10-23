# Данный блок вычисляет сумму двух чисел возвращая \
# значение и печатая пример в консоль.

from check_user_input import user_input_check as UI_check
from logger_user_action import logger_action as log
from color_out import out_green as green
from color_out import out_white as white


def sum_func(x):
    if x == 0:
        nums1 = UI_check(2, 0)
        nums2 = UI_check(2, nums1)
    else:
        nums1 = UI_check(2, 0, x)
        nums2 = UI_check(2, nums1)
    log(f'Ввел 1 число: {nums1}, второе: {nums2}.')
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 + nums2, 3)
        green(f'\n({nums1}) + ({nums2}) = {result} ')
        white('')
        log(f'получил результат: {result} .')
        return result
    elif isinstance(nums2, int| float) and isinstance(nums1, tuple) or \
        isinstance(nums2, tuple) and isinstance(nums1, int| float):
        result = []
        if isinstance(nums1, int| float):
            nums1, nums2 = nums2, nums1
        a = nums2 + nums1[0]
        if a != 0:
            result.append(str(a))
        b = nums1[1]
        if b != 0:
            if b < 0:
                result.append('-')
            elif b > 0:
                if a != 0:
                    result.append('+')
            if b == 1 or b == -1:
                result.append(nums1[2])
            else:
                result.append(str(abs(b)) + nums1[2])
        if len(result) == 0:
            result = 0
        else:
            result = ' '.join(result)
        log(f'получил результат: {result} .')
        green(f'\n({nums2}) + ({nums1[3]}) = {result} ')
        white('')
        return result
    else:
        result = []
        a =  nums1[0] + nums2[0]
        if a != 0:
            result.append(str(a))
        b = nums1[1] + nums2[1]
        if b != 0:
            if b > 0:
                if a != 0:
                    result.append('+')
            elif b < 0:
                result.append('-')
            if b == 1 or b == -1:
                result.append(nums2[2])
            else:
                result.append(str(abs(b)) + nums2[2])
        if len(result) == 0:
            result = 0
        else:
            result = ' '.join(result)
        log(f'получил результат: {result} .')
        green(f'\n({nums1[3]}) + ({nums2[3]}) = {result} ')
        white('')
        return result
