# Данный модуль вычисляет разность 2-х чисел.


from check_user_input import user_input_check as UI_check
from logger_user_action import logger_action as log


def subtraction_func(x):
    if x == 0:
        nums1 = UI_check(2, 0)
        nums2 = UI_check(2, nums1)
    else:
        nums1 = UI_check(2, 0, x)
        nums2 = UI_check(2, nums1)
    log(f'Ввел 1 число: {nums1}, второе: {nums2}.')
    result = None
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 - nums2, 3)
        print(f'({nums1}) - ({nums2}) = {result} ')
        log(f'получил результат: {result} .')
        return result
    if isinstance(nums2, int| float) and isinstance(nums1, tuple) or \
        isinstance(nums2, tuple) and isinstance(nums1, int| float):
        result = []
        if isinstance(nums1, int| float):
            nums1, nums2 = nums2, - nums1
            nums1[0] = - nums1[0]
        result.append(str(nums2 - nums1[0]))
        if nums1[1] < 0:
            result.append('-')
        else:
            result.append('+')
        result.append(str(abs(nums1[1])) + nums1[2])
        result = ' '.join(result)
        print(f'({nums2}) - ({nums1[3]}) = {result} ')
        return result
    else:
        result = []
        result.append(str(nums1[0] - nums2[0]))
        if nums1[1] - nums2[1] >= 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(abs(nums1[1] - nums2[1])) + nums2[2])
        result = ' '.join(result)
        print(f'({nums1[3]}) - ({nums2[3]}) = {result} ')
        log(f'получил результат: {result} .')
        return result