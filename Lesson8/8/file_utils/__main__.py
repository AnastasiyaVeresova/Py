import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from traverse_directory import main as traverse_directory_main
from json_to_pickle import json_to_pickle
from read_csv_and_process import read_csv_and_process
from save_data_to_csv import save_data_to_csv
from text_to_json import text_to_json
from users_id_to_json import users_id_to_json

if __name__ == "__main__":
    directory_to_scan = './'
    traverse_directory_main(directory_to_scan)

    json_to_pickle(directory_to_scan)

    csv_file_path = 'users.csv'
    json_file_path = 'processed_users.json'

    if os.path.exists(csv_file_path):
        read_csv_and_process(csv_file_path, json_file_path)
    else:
        print(f"Файл {csv_file_path} не найден.")

    json_file_path = 'users.json'
    csv_file_path = 'users.csv'

    if os.path.exists(json_file_path):
        save_data_to_csv(json_file_path, csv_file_path)
    else:
        print(f"Файл {json_file_path} не найден.")

    file_path = './res.txt'

    if os.path.exists(file_path):
        text_to_json(file_path)
    else:
        print(f"Файл {file_path} не найден.")

    users_id_to_json()
