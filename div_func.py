# Модуль производит деление.


from check_user_input import user_input_check as UI_check
from logger_user_action import logger_action as log


def division_func(x):
    if x == 0:
        nums1 = UI_check(2, 0)
        nums2 = UI_check(2, nums1)
    else:
        nums1 = UI_check(2, 0, x)
        nums2 = UI_check(2, nums1)
    log(f'Ввел 1 число: {nums1}, второе: {nums2}.')
    if nums2 == 0:
        print('\nМатематическая ошибка, на "0" делить нельзя!')
        log('пытается делить на "0", программа запросила повторный ввод.')
        nums2 = UI_check(2, nums1)
        if nums2 == 0:
            log('повторно  пытается делить на "0". программа отправила юзера в главное меню. вернув результат "0"')
            print('\nВыберите другую операцию.')
            return 0
    if isinstance(nums2, int| float) and isinstance(nums1, int| float):
        result = round(nums1 / nums2, 3)
        log(f'получил результат: {result} .')
        print(f'({nums1}) / ({nums2}) = {result} ')
        return result
    else:
        result = []
        nnums1 = []
        nnums2 = []
        if isinstance(nums1, int|float) and isinstance(nums2, tuple) :
            nnums1, nums1 = nums1, nnums1
            nums1.append(nnums1)
            nums1.append(0)
            nums1.append(nums2[2])
            nums1.append(str(nnums1))
        elif isinstance(nums2, int|float) and isinstance(nums1, tuple):
            nnums2, nums2 = nums2, nnums2
            nums2.append(nnums2)
            nums2.append(0)
            nums2.append(nums1[2])
            nums2.append(str(nnums2))
        result.append(str(round(((nums1[0] * nums2[0] + nums1[1] * nums2[1])/(nums2[0] ** 2 + nums2[1] ** 2)), 3)))
        if (nums2[0] * nums1[1] - nums1[0] * nums2[1])\
            /(nums2[0] ** 2 + nums2[1] **  2) >= 0:
            result.append('+')
        else:
            result.append('-')
        result.append(str(round(abs((nums2[0] * nums1[1] - nums1[0] * nums2[1])/ (nums2[0] ** 2 + nums2[1] ** 2)), 3)) + nums2[2])
        result = ' '.join(result)
        log(f'получил результат: {result} .')
        print(f'({nums1[3]}) / ({nums2[3]}) = {result} ')
        return result