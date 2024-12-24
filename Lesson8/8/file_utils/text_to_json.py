# Был сформирован файл с псевдоименами и произведениями чисел, напишите функцию, которая создает из созданного ранее файла новый в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки

import json
import os

def text_to_json(name='res.txt'):
    if not os.path.isfile(name):
        print(f"Файл {name} не найден.")
        return

    with open(name, 'r', encoding='utf-8') as f, \
         open('res.json', 'w', encoding='utf-8') as f2:
        res_list = []
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                name_part = parts[0].capitalize()
                product_part = parts[1]
                pair = {"name": name_part, "product": product_part}
                res_list.append(pair)
        json.dump(res_list, f2, indent=4)
