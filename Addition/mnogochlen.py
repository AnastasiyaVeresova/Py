# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.
# к = 2 -> -x^2 + 3^x - 8 = 0

import os
os.system("cls")

# int_array = [random.randint(-10,10) for i in range(number)]

import random

number = int(input("Введите натуральное число: "))
int_array = [random.randint(-10,10) for i in range(number)]
print(int_array)
strint_part = ""
for i in range(len(int_array)):
    if int_array[i] == 0:
        strint_part += 
#         if int_array[i] == 1:
#             strint_part += f"x^{len(int_array) - 1 - i} +"
#     else:
#         strint_part += f" {int_array[i]}*x^{len(int_array) - 1 - i} +"
        
# strint_part = strint_part.replace("+ -", "- ")[:-6]+" = 0"
# strint_part = strint_part.replace("^1", "")
print(strint_part)
