import csv
import json
import os

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_data_to_csv(json_file_path, csv_file_path):
    if not os.path.exists(json_file_path):
        print(f"Файл {json_file_path} не найден.")
        return

    data = load_data(json_file_path)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Access Level', 'User ID', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for access_level, users in data.items():
            for user_id, name in users.items():
                writer.writerow({'Access Level': access_level, 'User ID': user_id, 'Name': name})

    print(f"Данные успешно сохранены в файл {csv_file_path}")
