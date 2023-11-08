#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка; ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка; ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка; ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.    Ввод: ноутбук Вывод: 12

import os
os.system("cls")
# k = input().upper()
# count = 0
# if i in range ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'):
#     count =+ 1
# elif i in range ('D', 'G'):
#     count =+ 2
# elif i in range ('B', 'C', 'M', 'P'):
#     count =+ 3
# elif i in range ('F', 'H', 'V', 'W', 'Y'):
#     count =+ 4
# elif i in range ('K'):
#     count =+ 5
# elif i in range ('J', 'X'):
#     count =+ 8
# elif i in range ('Q', 'Z'):
#     count =+ 10
# if i in range ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'):
#     count =+ 1
# elif i in range ('Д', 'К', 'Л', 'М', 'П', 'У'):
#     count =+ 2
# elif i in range ('Б', 'Г', 'Ё', 'Ь', 'Я'):
#     count =+ 3
# elif i in range ('Й', 'Ы'):
#     count =+ 4
# elif i in range ('Ж', 'З', 'Х', 'Ц', 'Ч'):
#     count =+ 5
# elif i in range ('Ш', 'Э', 'Ю'):
#     count =+ 8
# elif i in range ('Ф', 'Щ', 'Ъ'):
#     count =+ 10
# print(count)

k = 'ноутбукъ'

# Введите ваше решение ниже
one_point = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'} #1
two_points = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'} #2
three_points = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'} #3
four_points = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'} #4
five_points = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'} #5
eight_points = {'J', 'X', 'Ш', 'Э', 'Ю'} #8
ten_points = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'} #10
total_points = 0

user_list = list()
for el in k:
    user_list.append(el.upper())
    

for i in user_list:
    if i in one_point: total_points += 1
    elif i in two_points: total_points += 2
    elif i in three_points: total_points += 3
    elif i in four_points: total_points += 4
    elif i in five_points: total_points += 5
    elif i in eight_points: total_points += 8
    elif i in ten_points: total_points += 10
    else: total_points += 0
    
print(total_points)




