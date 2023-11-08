# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста
# и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
import os
os.system("cls")
import random

'''
Решено через max_berries = max(new_list), но
Почему после 6 куста перестает работать выбор максимума через for max?

# for i in new_list:
#     max_berries = new_list[0]
#     if i > max_berries:
#         max_berries, i = i, max_berries
'''

# bush = 11
# berries = [8, 2, 15, 34, 65, 6, 7, 8, 9, 19, 11]

# bush = 5
# berries = [2, 4, 10, 4, 2]

# # bush = int(input('Введите количество кустов: '))
# # berries = []
# # for i in range(bush):
# #     berries.append(random.randint(1, 10))
# print(berries)
# new_list = []

# # for i in range (bush):
# #     while i < (len(berries)):
# #         sum = berries[i - 1] + berries[i] + berries[i - 2]
# #         for i in range (sum):
# #             if i == 0:
# #                 new_list.append(sum)
                
# for i in range (bush):
#     while i < (len(berries)):
#         sum = berries[i - 1] + berries[i] + berries[i - 2]
#         for i in range (sum):
#             if i == 0:
#                 new_list.append(sum)


# # for i in new_list:
# #     max_berries = new_list[0]
# #     if i > max_berries:
# #         max_berries, i = i, max_berries

# max_berries = max(new_list)

# print()
# print(*new_list) 
# print(max_berries)



import random
kust = int(input("введите количество кустов: "))
berryes = list(random.randint(0, 10) for i in range(kust))
result = []
i = 0
sum = 0

print(berryes)

while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(result)
print(f"максимальное число ягод за одну итерацию {result[-1]}")

# bush = 11
# # создание списка berries
# berries = []
# for i in range(bush):
#     berries.append(random.randint(1, 10))
# print(berries)

# # создание списка new_list - список сумм ягод с 3-х кустов
# new_list = []
# for i in range(len(berries)):
#     print(f'{i = }')
#     print(f'{berries[i - 2] = }')
#     print(f'{berries[i - 1] = }')
#     print(f'{berries[i] = }')
#     sum_ = berries[i - 1] + berries[i] + berries[i - 2]
#     new_list.append(sum_)
#     print(sum_)
#     print('*' * 15)

# print(*new_list)
# # функция max() находит максимум в списке new_list
# print(max(new_list))