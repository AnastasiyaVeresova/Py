# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод: values = [0, 2, 10, 6] same

# values = [0, 2, 10, 6]
# def same_by (characteristic, objects):
#     sq = list(filter(characteristic,objects))
#     if objects == sq or len(sq) == 0:
#         return True
#     return False

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# #-----------------------------------------------------

# values = [0, 2, 10, 6]
# def same_by (characteristic, objects):
#     sq = list(filter(characteristic,objects))
#     if  len(sq) == len(sq) % len(objects):
#         return True
#     return False

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


#-----------------------------------------------

# values = [0, 2, 10, 6]

# def same_by(characteristic, objects):
#     if len(set(map(characteristic, objects))) in (0, 1):
#         return True
#     return False

# print(same_by(lambda x: x % 2, values))
# print(same_by(lambda x: x % 2, []))
# print(same_by(lambda x: x > 2, values))

# #-------------------------------------------------

# list1 = [True, True]
# list2 = [False, False]
# print(all(list1))
# print(all(list2))

# list3 = [1, 1]
# list4 = [0, 0]
# print(all(list3))
# print(all(list4))

#------------------------------------
from functools import reduce
def is_same(func,values):
    return 'same' * reduce(lambda x,y: x == func(y),values, 1)+ ((1-reduce(lambda x,y: x == func(y),values,1))*'different')

a = [2,4,6,8]

is_same(lambda x: x%2==0,a)

#-------------------------------------
