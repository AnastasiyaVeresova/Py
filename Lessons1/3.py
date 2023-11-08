# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

import os

os.system("cls")

import math

school_class1 = int(input('Ведите количество учеников в 1 классе: '))
school_class2 = int(input('Ведите количество учеников в 2 классе: '))
school_class3 = int(input('Ведите количество учеников в 3 классе: '))

# print(math.ceil(school_class1/2) + math.ceil(school_class2/2) + math.ceil(school_class3/2))
# print((school_class1 // 2 + school_class1 % 2) + (school_class2 // 2 + school_class2 % 2) + (school_class3 // 2 + school_class3 % 2))
print((school_class1+1)//2 + school_class2//2 + (school_class2 % 2 != 0) + abs(-school_class3//2))

class1 = int(input('Введите количество учеников в первом классе: '))
class2 = int(input('Введите количество учеников во втором классе: '))
class3 = int(input('Введите количество учеников в третьем классе: '))

sum_desk = 0
for i in (class1, class2, class3):
    sum_desk += i // 2 + (i % 2)
print(sum_desk)