# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число. Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

import os

os.system("cls")

list_num = [1, 2, 3, 4, 5]
k = 3
# print(list_num)
# for i in range(k):
#     list_num.insert(0, list_num.pop())

#     print(list_num)

print(list_num[:k])
print(list_num[k:])

print(list_num[k:] + list_num[:k])

# sp = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     x = sp.pop()
#     sp.insert(0, x)
# print(sp)
