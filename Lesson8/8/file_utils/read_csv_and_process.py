# прочитайте созданный в csv файл без использования csv.DictReader
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной
# Добавьте поле хэш на основе имени и идентификатора
# Получившиеся записи сохраните в json
# Имя исходного и конечного файла передавайте как аргументы функции

import json
import hashlib
import os

def read_csv_and_process(csv_file_path, json_file_path):
    if not os.path.exists(csv_file_path):
        print(f"Файл {csv_file_path} не найден.")
        return

    data = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        headers = lines[0].strip().split(',')

        for line in lines[1:]:
            values = line.strip().split(',')
            record = {headers[i]: values[i] for i in range(len(headers))}

            user_id = record['User ID'].zfill(10)
            name = record['Name'].capitalize()
            hash_value = hashlib.sha256(f"{name}{user_id}".encode()).hexdigest()

            new_record = {
                'Access Level': record['Access Level'],
                'User ID': user_id,
                'Name': name,
                'Hash': hash_value
            }

            data.append(new_record)

    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    print(f"Данные успешно сохранены в файл {json_file_path}")
