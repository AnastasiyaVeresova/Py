# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит
import os

os.system("cls")

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list_ = []

for i in dictionary:
    for j in i:
        if i[j].strip() not in list_:
            list_.append(i[j].strip())
print("Вот все уникальные значения, которые есть в словаре: ", list_)

# sp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# unic = set()
# for i in sp:
#     for j in i:
#         unic.add(i[j].strip())
#     # unic.update(i.values()) #вернет уникальные значения
# print(unic)