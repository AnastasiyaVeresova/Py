# #Строки
# my_str = 'жило-было какое-то слово'
# if my_str.islower(): my_str.capitalize()#Проверит регистр и сделает первую букву заглавной, если регистр нижний
# my_str.find('какое-то слово') #строковый метод выдаст индекс вхождения введенного текста
# s.startswith(prefix) #Если начинается на него вернет True либо -1
# s.endswith(suffix) #Если оканчивается на него вернет True либо False
# my_str.replace('', '') #Заменяет первое на второе
# st = my_str.split(',') #Разобьет строку на подстроки по заданному разделителю
# s.partition(x) #Разбивает строку на части по разделителю x и разрезает строку на 3 части. Возвращает кортеж
# ','.join(st) #Соединит полученные ранее строки обратно
# s.title() #Первые буквы всех слов в верхний регистр - остальные в нижний
# s.upper() #Все в верхний регистр
# s.lower() #Все в нижний регистр
# s.swapcase() # Преобразует верхний в нижний и наоборот
# s.isupper() #Возвращает True, если все символы строки заглавные, иначе False
# s.istitle() #Определяет, начинаются ли слова строки с заглавной буквы
# s.replace(old, new)


# # Списки
# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# sp = [77, 88.88, True, "Hello"]
# sp.append(647) #добавит в конец
# sp += [1,2] #Кокантенация в конец = sp.extend(1,2)
# sp.extend(1,2) #Кокантенация в конец
# sp.insert(0, False) # Добавит эл-т False на нужную позицию
# print(sp)
# sp.count(1) #Посчитает сколько раз встречается 1 в списке
# sp.reverse() #Разворачивает список
# print(sp[2:6])
# print(sp[-2]) # Обратится к предпоследнему эл-ту
# a = sp.pop() #вырежет последний (если задать индекс - вырежет его)
# print(a)
# del sp[0] # Удалит эл-т по индексу
# sp.remove(True) # Удаляет первое вхождение слева - направо по значению
# print(sp)
# for item in sp:
# 	print(item) # Выведет все эл-ты по очереди
# for i in range(len(sp)): 
# 	print(sp[i])  # Выведет все эл-ты по очереди, обратится по индексу
# for i, value in enumerate(sp): #выведет ключ и значение без скобок друг под другом
# 	print(i, value)

# # Кортежи

# t1 = tuple(sp) # нельзя менять эл-ты, из списка сделали кортеж
# print(t1)
# print(t1[0])
# # распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# # Словари

# d = {"Ваня": 89217362453, "Вася": 81119362452}
# print(d["Ваня"]) #выведет его тел
# d["Сергей"] = 555555 # Добавит Сергея и номер
# print(d)
# print(d.keys()) # Пройтись по ключам
# print(d.values()) # Пройтись по значениям
# for key, value in d.items(): #выведет ключ и значение без скобок друг под другом - items возвращает пары
# 	print(key, value)

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# dictionary.update([other]) #Обновит словарь, создав пары(ключ, значение) из словаря other. Существующие ключи перезаписываются. Возвращает none! (не новый словарь)
	
# # Множества - неупорядоченная структура

# s = {77,77,77,8,9,11}
# s.add(1000) # добавит элемент
# s.discard(9) # если такой эл-т есть - удалит
# s.remove(9) # удаляет эл-т, а если его нет - выдает ошибку
# s.pop() #Удалит первый элемент
# len(s) #Число э-в в множестве
# x in s # Принадлежит ли x множеству s



# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# # 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
# 	list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# # 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# # Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0 ]# [(2, 2), (4, 4),..., (100, 100)]
# # Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# # В Python можно перемножать строку на число.
# def new_string(symbol, count):
# 	return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# def new_string(symbol, count=3):
# 	return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

#Модули

import calendar
print(dir(calendar)) #['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_get_default_locale', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']

print(calendar.calendar(2023))