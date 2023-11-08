import os
os.system("cls")
# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь. Через строку решать нельзя.


number = input('Введите чмсло для подсчета суммы его цифр: ')
def sum(number):
    res = 0
    for i in number:
        i = int(i)
        res += i
    return res 

print(sum(number))
