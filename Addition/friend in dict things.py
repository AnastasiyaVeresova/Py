# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Код должен расширяться на любое большее количество друзей.
import os
os.system("cls")

hike = {
'Aaz': ("спички", "спальник", "дрова", "топор", "петрушка"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),
}

# for keys, values in hike.items():
# #Aaz ('спички', 'спальник', 'дрова', 'топор')
# #Skeeve ('спальник', 'спички', 'вода', 'еда')
# #Tananda ('вода', 'спички', 'косметичка')
# 	print(keys, values)

# print(hike.items()) #dict_items([('Aaz', ('спички', 'спальник', 'дрова', 'топор')), ('Skeeve', ('спальник', 'спички', 'вода', 'еда')), ('Tananda', ('вода', 'спички', 'косметичка'))])

#print(set(hike.items())) ##{('Tananda', ('вода', 'спички', 'косметичка')), ('Skeeve', ('спальник', 'спички', 'вода', 'еда')), ('Aaz', ('спички', 'спальник', 'дрова', 'топор'))}

#print(hike.values()) #dict_values([('спички', 'спальник', 'дрова', 'топор'), ('спальник', 'спички', 'вода', 'еда'), ('вода', 'спички', 'косметичка')]) 

#print(hike.keys(), set(hike.values())) #dict_keys(['Aaz', 'Skeeve', 'Tananda']) {('спальник', 'спички', 'вода', 'еда'), ('вода', 'спички', 'косметичка'), ('спички', 'спальник', 'дрова', 'топор')}

# print(hike.keys()) #dict_keys(['Aaz', 'Skeeve', 'Tananda'])
# print(set(hike)) #{'Aaz', 'Skeeve', 'Tananda'}

# print(hike[next(iter(hike.keys()))]) #('спички', 'спальник', 'дрова', 'топор')

# print(hike[list(hike.keys()) [0]]) #('спички', 'спальник', 'дрова', 'топор')

# print(next(iter(hike.keys()))) #Aaz

# print(hike[list(hike.keys()) [-1]]) #('вода', 'спички', 'косметичка')

# print(list(hike.keys()) [-1]) #Tananda
#######################################################################################################
for friend, things in hike.items():
    if type(hike[friend]) == int:
        print(1)
    else:
        print(f'{friend} взял с собой {len(set(things))} вещи(ей):', things)

print()

#######################################################################################################
# print(len(hike)) #3
# output = len(hike)
# print(output) #3
# print(len(hike.values()))#3
# print(len(hike.keys()))#3
#######################################################################################################
print('---> Kакая вещь есть у каждого из друзей?')
for friend, things in hike.items():
    common_things = set(hike[next(iter(hike.keys()))])
print("У каждого из друзей есть: ",*set(common_things.intersection(things)))
print()

##-------------------------------------------------------------------------------------------
# common_items = set(hike['Aaz'])
# for friend, items in hike.items():
#     common_items = common_items.intersection(set(items))
# print("Все три друга взяли: ",*common_items)

##-------------------------------------------------------------------------------------------
# for friend, things in hike.items():
# 	common_things = set(hike[list(hike.keys()) [0]])
# 	common_things = common_things.intersection(things)
# print("Все три друга взяли: ",*common_things)

######################################################################


print('---> Какие теперь у друзей есть вещи в совокупности?')
print("Эти вещи есть в совокупности: ", set((hike['Aaz']) + (hike['Skeeve']) + (hike['Tananda'])))
# {'топор', 'дрова', 'спички', 'еда', 'вода', 'спальник', 'косметичка'}
print()

#######################################################################################################
print('---> Kакие в совокупности вещи уникальны, есть только у одного из друзей?')
for friend, things in hike.items():
    friend_1st = set(hike[next(iter(hike.keys()))])
    friend_2nd = set(hike[list(hike.keys()) [1]])
    friend_3rd = set(hike[list(hike.keys()) [-1]])
    if friend_1st:
        print(f'Только у', list(hike.keys()) [0], 'есть: ', *friend_1st.difference(friend_2nd).difference(friend_3rd))
        # break
    if friend_2nd:
        print(f'Только у', list(hike.keys()) [1], 'есть: ', *friend_2nd.difference(friend_3rd).difference(friend_1st))
        # break
    if friend_3rd:
        print(f'Только у', list(hike.keys()) [-1], 'есть: ', *friend_3rd.difference(friend_1st).difference(friend_2nd))
        break
print()

##--------------------------------------------------------------------------------------------------
uniq_items = set()
all_items = set()
for friend, things in hike.items():
    for friend in things:
        if friend in all_items:
            uniq_items.discard(friend)
        else:
            uniq_items.add(friend)
        all_items.add(friend)
print("Уникальные вещи: ",*uniq_items)
print()
######################################################################


print('---> Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?')

for friend, things in hike.items():
    if friend_1st:
        print(f'Только у', list(hike.keys()) [0], 'нет: ', *((friend_2nd).union(friend_3rd)).difference(friend_1st))
        # break
    if friend_2nd:
        print(f'Только у', list(hike.keys()) [1], 'нет: ', *((friend_3rd).union(friend_1st)).difference(friend_2nd))
        # break
    if friend_3rd:
        print(f'Только у', list(hike.keys()) [-1], 'нет: ', *((friend_2nd).union(friend_1st)).difference(friend_3rd))
        break
print()

all_except_one = {}
for item in all_items:
    for friend, things in hike.items():
        if item not in things:
            all_except_one.setdefault(item, []).append(friend)
print("Вещи, которые есть у всех, кроме одного: ")
for item, friends in all_except_one.items():
    print(f"{item} отсутствует(-ют) у {', '.join(friends)}")
