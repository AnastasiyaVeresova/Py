def hello(name):
    return "hello, " + name

def byebye(name):
    return name + ", bye bye"

def create_phrase(func):
    name = input("Введите свое имя ") #1
    return func(name)     # 3

def create_two_phrase(funcs):
    name = input("Введите свое имя ") #1
    res = ""
    for func in funcs:
        res += func(name) +"\n"
    return res     # 3

# print(create_phrase(hello))
# print(create_phrase(byebye))
# funcs = (hello, byebye)
# print(create_two_phrase(funcs))
_____________________________________________________________________________
# Мы можем вернуть функцию внутри функции. Рассмотрим создание
# функции, позволяющей вычислить любое число в любой степени.
# Сделаем функцию calc_power, которая на входе принимает степень, а
# внутри нее создадим функцию power, которая принимает число.

def calc_power(degree):
    def power(num):
        return num ** degree
    return power

# print(calc_power(3) (2) )

cube = calc_power(3)
square = calc_power(2)

print(cube(4))
print(square(9))

__________________________________________________________________________
calc_pw = lambda x,y: x**y if x < y else False
print(calc_pw(4, 3))
