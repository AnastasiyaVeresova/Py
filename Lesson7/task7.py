# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int, второе - float 
# разделены вертикальной чертой, миниимальное число - -1000, максимальное - +1000. Количество строк и имя файла передаются как аргументы функции

# import os
# import random as rd

# MIN_NUMBER = -1000
# MAX_NUMBER = 1000

# def generate_number_file(count:int, filename:str):
#     """Заполняет файл случайными числами"""
#     with open(filename, 'w', encoding='utf-8') as f:
#         for i in range(count):
#             f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)}|{rd.random() * 2000 - 1000}\n')

# if __name__ == '__main__':
#     generate_number_file(10, 'data.txt')

    # Напишите функцию, которая генерирует псевдоимена.
    # имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
    # Полученные имена сохраняются в файл

# import random

# MIN_LEN = 4
# MAX_LEN = 7
# MIN_LETTER = ord('a')
# MAX_LETTER = ord('z')
# VOWELS = ('a', 'o', 'y', 'i', 'u', 'e')

# def generate_name_file(filename: str, count_name: int):
#     with open(filename, 'w', encoding='utf-8') as fs:
#         for _ in range(count_name):
#             while True:
#                 len_name = random.randint(MIN_LEN, MAX_LEN)
#                 name = [chr(random.randint(MIN_LETTER, MAX_LETTER)) for _ in range(len_name)]
#                 if any(letter in VOWELS for letter in name):
#                     break
#                 # Если гласных нет, добавим одну гласную в случайное место
#                 index = random.randint(0, len_name - 1)
#                 name[index] = random.choice(list(VOWELS))

#             name = ''.join(name).capitalize()
#             fs.write(name + '\n')

# if __name__ == '__main__':
#     generate_name_file('data_names.txt', 15)

# =================================

# import random
    
# MIN_LEN = 4
# MAX_LEN = 7
# MIN_LETTER = ord('a')
# MAX_LETTER = ord('z')
# VOWELS = ('a', 'o', 'y', 'i', 'u', 'e')
    

# def generate_neme_file(filename:str, count_name: int):
#     with open(filename, 'w', encoding='utf-8') as fs:
#         for j in range(count_name):
#             len_name = random.randint(MIN_LEN, MAX_LEN)
#             name = []
#             for i in range(len_name):
#                 name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
#             has_vowels = False
#             for letter in name:
#                 if letter in VOWELS:
#                     has_vowels = True
#                     break
#                 if not has_vowels:
#                     index = random.randint(0, len_name - 1)
#                     letter = random.choice(list(VOWELS))
#                     name[index] = letter
#                 print(f'{"".join(name).capitalize()}', file = fs, end='')
#                 fs.write('\n' if j < count_name - 1 else "")

# if __name__ == '__main__':
#     generate_neme_file('data_names.txt', 15)
# ==========================

# def read_line_or_begin(fd) -> str:
#     text = fd.readline()
#     if text == '':
#         fd.seek(0)
#         text = fd.readline()
#     return text.strip()


# def process_files(file_numbers, file_names, file_res):
#     with open(file_numbers, 'r', encoding='utf-8') as f_num:
#         with open(file_names, 'r', encoding='utf-8') as f_name:
#             with open(file_res, 'w', encoding='utf-8') as f_res:
#                 # Читаем все строки, чтобы определить длину файлов
#                 lines_num = f_num.readlines()
#                 lines_name = f_name.readlines()
#                 length1 = len(lines_num)
#                 length2 = len(lines_name)
#                 length = max(length1, length2)
                

#                 # Возвращаем указатель в начало файлов
#                 f_num.seek(0)
#                 f_name.seek(0)

#                 for i in range(length):
#                     line_num = read_line_or_begin(f_num)
#                     line_name = read_line_or_begin(f_name)
#                     if line_num and line_name:
#                         a, b = line_num.split('|')
#                         a = int(a)
#                         b = float(b)
#                         res = a * b
#                         if res < 0:
#                             res *= -1
#                             line_name = line_name.lower()
#                         else:
#                             res = round(res)
#                             line_name = line_name.upper()
#                         f_res.write(f'{line_name} {res}')
#                         f_res.write('\n' if i < length - 1 else "")

# if __name__ == '__main__':
#     process_files('data.txt', 'data_names.txt', 'f_res.txt')


# ==========================================

import random
import os

MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
    


def generate_text(length):
            """Генерирует случайное имя файла"""

            name = []
            for i in range(length):
                name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
            return "".join(name)

def generate_files(extension:str,
                   directory:str,
                   min_length=6,
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
    """Генерирует файлы с заданными параметрами"""
    if not os.path.exists(directory) or not os.path.isdir(directory):
           os.mkdir(directory)

    for i in range(num_files):
           name_length = random.randint(min_length, max_length)
           filename = generate_text(name_length)
           text_length = random.randint(min_bytes, max_bytes)
           text = generate_text(text_length)
           while True:
                try:
                         with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                            f.write(text)
                except:
                       filename = generate_text(name_length)
                else:
                       break

if __name__ == '__main__':
        generate_files('rnd', 'files')
    