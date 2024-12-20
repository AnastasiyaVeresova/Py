# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def parse_file_path(file_path):
    path, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    return path, name, extension


file_path = "/home/user/documents/example.txt"
path, name, extension = parse_file_path(file_path)
print(f"Путь: {path}, Имя файла: {name}, Расширение: {extension}")

# Путь: /home/user/documents, Имя файла: example, Расширение: .txt


# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def calculate_bonuses(names, rates, bonuses):
    return {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}


names = ["Катя", "Миша", "Саша"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5.5%", "8.75%"]

bonus_dict = calculate_bonuses(names, rates, bonuses)
print(bonus_dict)

# {'Катя': 102.5, 'Миша': 82.5, 'Саша': 175.0}

# 4. Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def gen_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

fib_gen = gen_fib()

for i in range(1, 11):
    print(f'{i}: {next(fib_gen)}')


