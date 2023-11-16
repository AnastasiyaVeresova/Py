def hello(name):
    return "hello, " + name

def byebye(name):
    return name + ", bye bye"

def create_phrase(func):
    name = input("Введите свое имя ")
    return func(name)

print(create_phrase(hello))

# Мы можем вернуть функцию внутри функции. Рассмотрим создание
# функции, позволяющей вычислить любое число в любой степени.
# Сделаем функцию calc_power, которая на входе принимает степень, а
# внутри нее создадим функцию power, которая принимает число.

def calc_power(degree):
    def power(num):
        return num ** degree
    return power
