# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках. Ввод: Вывод: 1 2 3 2 3 2

# # print(sp:=[random.randint(1,10) for _ in range(6)])
# sp = [9, 4, 4, 7, 5, 3, 8, 5, 5, 5, 5, 5]
# print (sp)
# counter = 0
# for i in set(sp):
#     counter += sp.count(i) // 2
# print(counter)
# print(sum([sp.count(i) // 2 for i in set(sp)]))

#----------------------------------
import random

def create_random_list(num):
    return [random.randint(0, 2) for _ in range(num)]

def find_couple(_user_list_: list):
    count_of_couple = 0
    for i in set(_user_list_):
        count_of_couple += _user_list_.count(i) // 2
    return count_of_couple

len_list = int(input("Введите длину массива: "))

user_array = create_random_list(len_list)

print(user_array)
print(find_couple(user_array))