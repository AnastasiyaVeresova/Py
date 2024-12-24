
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


import random
    
MIN_LEN = 4
MAX_LEN = 7
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
VOWELS = ('a', 'o', 'y', 'i', 'u', 'e')
    

def generate_name_file(filename:str, count_name: int):
    with open(filename, 'w', encoding='utf-8') as fs:
        for j in range(count_name):
            len_name = random.randint(MIN_LEN, MAX_LEN)
            name = []
            for i in range(len_name):
                name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
            has_vowels = False
            for letter in name:
                if letter in VOWELS:
                    has_vowels = True
                    break
                if not has_vowels:
                    index = random.randint(0, len_name - 1)
                    letter = random.choice(list(VOWELS))
                    name[index] = letter
                print(f'{"".join(name).capitalize()}', file = fs, end='')
                fs.write('\n' if j < count_name - 1 else "")

if __name__ == '__main__':
    generate_name_file('data_names.txt', 15)