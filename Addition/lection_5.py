
def f(x):
    return x*x
a = f
print(f(5))
print(a(5))
 
____________________________________________________________________миникалькулятор
 
def calc1(a, b):
    return a + b
   
def calc2(a, b):
    return a * b
   
def math(op, x, y):
    print(op(x, y))
   
math(calc2, 5, 7)
 
-------------------------------------
 
# calc1 = lambda a,b: a + b
   
math(lambda a,b: a + b, 5, 7)
 
 
___________________________________________________
data = [1, 2, 3, 5, 8, 15, 23, 38]
result = []
 
for i in data:
    if i % 2 == 0:
        result.append((i, i**2))
 
print(result)
 
# [(2, 4), (8, 64), (38, 1444)]
 
________________________________________________lambda function
 
def select(f, col):
    return [f(x) for x in col]
   
def where(f, col):
    return [x for x in col if f(x)]
   
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
 
#[1, 2, 3, 5, 8, 15, 23, 38]
#[2, 8, 38]
 
_______________________________________________________________
 
def select(f, col):
    return [f(x) for x in col]
   
def where(f, col):
    return [x for x in col if f(x)]
   
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
 
# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]
 
-------------------------------------------------
 
def where(f, col):
    return [x for x in col if f(x)]
   
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = where(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)
 
# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]
 
_____________________________________________map
list_1 = [x for x in range(1, 20)]
print(list_1)
 
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
 
____________________________________________________________________
С клавиатуры вводится некий набор чисел через пробел, этот набор чисел считывается как строка.
Как превратить лист строк в list чисел?
 
data = '15 156 96 3 5 8 52 5'
# print(data)
# data = data.split()
# print(data)
## 15 156 96 3 5 8 52 5
## ['15', '156', '96', '3', '5', '8', '52', '5']
 
 
data = list(map(int, data.split()))
print(data)
 
# [15, 156, 96, 3, 5, 8, 52, 5]
 
___________________________________________________________________filter
 
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
 
# [15, 65, 175]
 
_________________________________________________________________
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
 
# [(2, 4), (8, 64), (38, 1444)]
______________________________________________________________________zip
zip([1, 2, 3], ['o', 'д', 'т'], ['f', 's', 't'])
#[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
______________________________________________________________________enumerate
 
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
 
#[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
--------------------------------------------
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)
 
##[(0, 'user1'), (1, 'user2'), (2, 'user3')]
_______________________________________________________________________файлы
 
colours = ['red', 'green', 'blue']
data = open('file.txt', 'a') #указываем режим, в котором будем работать(создастся, если нет)
data.writelines(colours) #разделителей не будет
data.close()
 
 
with open(file.txt, 'w') as data:  #(перезапишет все)
                data.write('line 1\n')     #\n с новой строки
                data.write('line 2\n')
 
 
path = 'file.txt'                
data = open('file.txt', 'r')               #(чтение)
for line in data:
                print(line)
data.close()
 
______________________________________________________________________os modul
 
import os
 
print(os.chdir(path))                  #смена текущей директории
print(os.getcwd())                  #теущая рабочая директория
print(os.path.basename(path))                  #базовое имя пути
print(os.path.abspath('main.py'))     #возвращает нормализованный абсолютный путь
 
________________________________________________________________________shutil modul
 
import shutil
 
shutil.copyfile(src, dst)         #копирует содержимое (но не метаданные) файла src в файл dst
shutil.copy(src, dst)         #копирует содержимое файла src в файл или папку dst
shutil.rmtree(path)         #удаляет текущую директорию и все поддиректории; path должен
                                                               #указывать на директорию, а не на символическую ссылку


