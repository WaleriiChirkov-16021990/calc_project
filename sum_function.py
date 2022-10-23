# Данный блок вычисляет сумму двух чисел возвращая \
# значение и печатая пример в консоль.


from check_user_input import user_input_check as UI_check
from logger_user_action import logger_action as log


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
        print(f'({nums1}) + ({nums2}) = {result} ')
        log(f'получил результат: {result} .')
        return result
    if isinstance(nums2, int| float) and isinstance(nums1, tuple) or \
        isinstance(nums2, tuple) and isinstance(nums1, int| float):
        result = []
        if isinstance(nums1, int| float):
            nums1, nums2 = nums2, nums1
        result.append(str(nums2 + nums1[0]))
        if nums1[1] < 0:
            result.append('-')
        else:
            result.append('+')
        result.append(str(abs(nums1[1])) + nums1[2])
        result = ' '.join(result)
        print(f'({nums2}) + ({nums1[3]}) = {result} ')
        return result
    else:
        result = []
        a =  nums1[0] + nums2[0]
        if a != 0:
            result.append(a)
        b = nums1[1] + nums2[1]
        if b != 0:
            if b > 0:
                if a != 0:
                    result.append('+')
            else:
                result.append('-')
            if b == 1 or b == -1:
                result.append(nums2[2])
            else:
                result.append(str(abs(b)) + nums2[2])
        if len(result) == 0:
            result.append(0)
        result = ' '.join(result)
        log(f'получил результат: {result} .')
        print(f'({nums1[3]}) + ({nums2[3]}) = {result} ')
        return result