# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#             max_number = n
# print(max_number)
        
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)

# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

import os
os.system("cls")



import random
sequence = [random.randint(0,20) for _ in range(10)]
print(sequence)
max_value = 0 
found_zero = False

for num in sequence:
    if sequence[0] == 0:
        print("0 находится на 1 месте в последовательности, максимального числа до него нет")
        found_zero = True
        break
    if num == 0:
        print("Наибольшее значение, завершающееся первым встретившимся нулем:", max_value)
        found_zero = True
        break
    elif num > max_value:
        max_value = num

if found_zero == False:
    print("В последовательности нет нуля")

# from random import randint
# sequence = []
# def build_seq():
#     sequence = [randint(0,10) for _ in range(20)]
#     while (sequence[0] == 0 and len(sequence) > 0):
#         sequence = sequence[1:]
#     return sequence

# while(len(sequence) == 0):
#    sequence = build_seq()

# sequence.insert(randint(1,len(sequence)),0)
# maxnumber = 0
# for i in sequence:
#     if i == 0:
#         break
#     elif(maxnumber<i):
#         maxnumber = i

# print(sequence)
# print(maxnumber)
