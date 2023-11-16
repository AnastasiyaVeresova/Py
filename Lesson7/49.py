# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде 20 минутСеминар 7. Функции высшего порядка Задача №49.
# Решение в группах Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits)) Вывод: 2.5 10

# orbits = [(1, 3), (7, 2), (6, 6), (4, 3),(2.5, 10)]
# sq = [(item[0]*item[1]) if item[0]!=item[1] else 0 for item in orbits ]
# print(orbits[sq.index(max(sq))])

# sq = list(map(lambda x: x[0]*x[1] if x[0]!=x[1] else 0,orbits))
# print(orbits[sq.index(max(sq))])

# print(orbits.index(*filter(lambda item: item[0]*item[1]== max(list(map(lambda x:\
#                     x[0]*x[1] if x[0]!=x[1] else 0,orbits))), orbits)))
# # (2.5, 10)
# # (2.5, 10)
# # 4

import math
from math import pi
def find_farthest_orbit(list_of_orbits):
    areas=[]
    max_area = 0
    max_el= list_of_orbits[0]
    max_area2=max([pi*i[0]*i[1] for i in list_of_orbits if i[0] != i[1]])
    res_final= list(filter(lambda x: max_area2 == pi*x[0]*x[1] ,list_of_orbits))
    return res_final[0]
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farthest_orbit(orbits))

#--------------------------------------------

def find_farthest_orbit(list_of_orbits):
    return max(list(filter(lambda x: x[0] != x[1],list_of_orbits)), key = lambda x: math.pi*x[0]*x[1])
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
