# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему! Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза Input: 5 -> 5 1 6 5 9 Output: 1 9

import os
import random

os.system("cls")

# N = int(input("Введите число арбузов "))
# max = 0
# min = 999

# for i in range(N):
#     mass = random.randint(1, 10)
#     print(mass, end=' ')
#     if mass <= min:
#         min = mass
#     if mass >= max:
#         max = mass
# print()
# print("Самый тяжелый арбуз весит: ", max)
# print("Самый легкий арбуз весит: ", min)

n = int(input("Введите число арбузов "))
mass_list = []
for i in range(n):
    mass_list.append(random.randint(1, 10))
print(mass_list)
# print(min(mass_list), max(mass_list))
min_ = mass_list[0]
max_ = mass_list[0]
for i in mass_list:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
print()
print(min_, max_)

# n = int(input('Введите количество арбузов: '))
# watermelon = []
# for i in range(n):
#     watermelon.append(int(input()))
# print(max(watermelon), min(watermelon))

