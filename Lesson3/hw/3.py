# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

lst = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 1]
print(find_duplicates(lst))  # Вывод: [1, 2, 3]


# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

# def top_10_words1(text):
#     # Удаляем все символы, кроме букв, цифр и пробелов, и приводим к нижнему регистру
#     text = re.sub(r'[^\w\s]', '', text).lower()
#     words = text.split()

#     # Создаем словарь для подсчета частоты слов
#     word_counts = {}
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1

#     # Сортируем словарь по частоте слов и выбираем 10 самых частых
#     sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
#     most_common = sorted_word_counts[:10]

#     return most_common


def top_10_words2(text):
    #  регулярное выражение для удаления всех символов, кроме букв, цифр и пробелов, и приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)
    return most_common

text = """
Python is an interpreted, high-level, \ general-purpose programming language. Created by Guido van Rossum and first released in 1991, \ Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs \ and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""
# print(top_10_words1(text))
print(top_10_words2(text))

# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. \ Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. \ Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
    
def find_combinations(items, max_weight, current_combination=[]):
    # Если текущая комбинация вещей превышает максимальную грузоподъёмность, возвращаем пустой список
    if sum(items[item] for item in current_combination) > max_weight:
        return []

    # Если текущая комбинация вещей точно равна максимальной грузоподъёмности, возвращаем её
    if sum(items[item] for item in current_combination) == max_weight:
        return [current_combination]

    # Иначе, продолжаем генерировать комбинации
    valid_combinations = []
    for item in items:
        if item not in current_combination:
            new_combination = current_combination + [item]
            valid_combinations.extend(find_combinations(items, max_weight, new_combination))

    return valid_combinations

# Пример использования
items = {
    "tent": 5,
    "sleeping_bag": 3,
    "water": 2,
    "food": 4,
    "clothes": 3,
    "flashlight": 1,
    "map": 1
}

max_weight = 10

valid_combinations = find_combinations(items, max_weight)

for index, combination in enumerate(valid_combinations, start=1):
    print(f"{index}. {combination}")