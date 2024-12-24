# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноименных pickle файлов
import os
import json
import pickle

def json_to_pickle(directory=''):
    # Проверяем, существует ли указанная директория
    if not os.path.isdir(directory):
        print(f"Директория {directory} не существует.")
        return

    json_files_found = False

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        # Проверяем, является ли файл JSON файлом
        if filename.endswith('.json'):
            json_files_found = True
            json_path = os.path.join(directory, filename)
            pickle_path = os.path.join(directory, filename.replace('.json', '.pickle'))

            # Читаем содержимое JSON файла
            with open(json_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # Сохраняем содержимое в pickle файл
            with open(pickle_path, 'wb') as pickle_file:
                pickle.dump(data, pickle_file)

            print(f"Файл {json_path} успешно сохранен в {pickle_path}")

    if not json_files_found:
        print('JSON файлы отсутствуют')

if __name__ == "__main__":
    directory = './'  # Укажите путь к вашей директории
    json_to_pickle(directory)
