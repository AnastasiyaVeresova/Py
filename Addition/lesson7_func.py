def hello(name):
    return "hello, " + name

def byebye(name):
    return name + ", bye bye"

def create_phrase(func):
    name = input("Введите свое имя ")
    return func(name)

print(create_phrase(hello))
