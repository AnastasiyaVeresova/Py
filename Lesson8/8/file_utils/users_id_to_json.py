# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7)
# После каждого ввода добавляйте новую информацию в JSON файл
# Пользователи группируются по уровню доступа
# Идентификатор пользователя выступает ключем для имени
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа
# При перезапуске функции уже записанные в файл данные должны сохраняться

import json
import os

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def users_id_to_json():
    print("Для выхода введите 'exit' на любом этапе.")

    file_path = 'users.json'
    data = load_data(file_path)

    while True:
        name = input("Введите имя: ")
        if name.lower() == 'exit':
            print("Программа завершает свою работу.")
            break

        user_id = input("Введите личный идентификатор: ")
        if user_id.lower() == 'exit':
            print("Программа завершает свою работу.")
            break

        access_level = input("Введите уровень доступа (от 1 до 7): ")
        if access_level.lower() == 'exit':
            print("Программа завершает свою работу.")
            break

        if not access_level.isdigit() or int(access_level) < 1 or int(access_level) > 7:
            print("Неверный уровень доступа. Пожалуйста, введите число от 1 до 7.")
            continue

        access_level = int(access_level)

        # Проверка уникальности идентификатора
        if any(user_id in users for users in data.values()):
            print("Идентификатор должен быть уникальным. Пожалуйста, введите другой идентификатор.")
            continue

        if access_level not in data:
            data[access_level] = {}

        data[access_level][user_id] = name

        save_data(file_path, data)
        print(f"Пользователь {name} с идентификатором {user_id} и уровнем доступа {access_level} добавлен.")

if __name__ == "__main__":
    users_id_to_json()
