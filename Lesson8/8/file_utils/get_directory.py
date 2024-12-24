# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            is_file = os.path.isfile(full_path)
            size = os.path.getsize(full_path) if is_file else get_directory_size(full_path)
            results.append({
                'path': full_path,
                'parent': root,
                'type': 'file' if is_file else 'directory',
                'size': size
            })

    return results

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['path', 'parent', 'type', 'size']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def main(directory):
    data = traverse_directory(directory)
    save_to_json(data, 'results.json')
    save_to_csv(data, 'results.csv')
    save_to_pickle(data, 'results.pickle')

if __name__ == "__main__":
    directory_to_scan = './'
    main(directory_to_scan)
