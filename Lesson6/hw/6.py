# # В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

from datetime import datetime as dt
from calendar import isleap
import argparse


def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True
    except:
        return False


def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")


def main():
    parser = argparse.ArgumentParser(description='Проверка даты на корректность.')
    parser.add_argument('date', type=str, help='Дата в формате DD.MM.YYYY')
    args = parser.parse_args()
    

    date = args.date
    if check_date(date):
        print(f"Дата {date} корректна.")
    else:
        print(f"Дата {date} некорректна.")
        

if __name__ == '__main__':
    main()
    
# # python 6.py 25.06.1984

# # 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def is_valid_queens(positions):
    def is_attacking(q1, q2):
        return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if is_attacking(positions[i], positions[j]):
                return False
    return True


positions = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(is_valid_queens(positions))  # Вывод: False

# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def is_valid_queens(positions):
    def is_attacking(q1, q2):
        return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if is_attacking(positions[i], positions[j]):
                return False
    return True


def generate_random_positions():
    positions = []
    for i in range(1, 9):
        y = random.randint(1, 8)
        positions.append((i, y))
    return positions


def find_successful_positions(num_successes):
    successful_positions = []
    attempts = 0
    # max_attempts = 10000  # Limit the number of attempts
    # while len(successful_positions) < num_successes and attempts < max_attempts:
    while len(successful_positions) < num_successes:

        positions = generate_random_positions()
        if is_valid_queens(positions):
            successful_positions.append(positions)
            # print(f"Найдена успешная расстановка {len(successful_positions)}: {positions}")
        attempts += 1
    return successful_positions


if __name__ == "__main__":
    successful_positions = find_successful_positions(4)
    if successful_positions:
        for i, positions in enumerate(successful_positions, 1):
            print(f"Успешная расстановка {i}: {positions}")
    else:
        print("Не удалось найти успешные расстановки в пределах лимита попыток")
