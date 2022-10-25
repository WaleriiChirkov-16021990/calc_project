# import re

# def check_3_complex(x):
#     math = re.search(r'\D?\d+\D{1}\d+[+-]\d+\D{1}\d+\D{1}', x)
#     return True if math else False

# def sub_float(x: str):
#     y = None
#     if x[0] == '-':
#         y = re.sub(r'^\D?\d*\D{1}\d*?\w{1}$', f'0{x}', x, 1)
#         return y if y else False
#     if x[0].isdigit():
#         y = re.sub(r'\D?\d*\D{1}\d*\w{1}', f'0+{x}', x, 1)
#         return y if y else False
#     if x[0].isalpha():
#         y = re.sub(r'\w{1}', f'0+1{x}', x, 1)
#         return y if y else False


# i = '5 - 5i'

# print(check_3_complex(i))
# print(sub_float(i))