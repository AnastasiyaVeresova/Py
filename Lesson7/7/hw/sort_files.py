import os
from generate_files import generate_files

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'img',
    'png': 'img',
}

def generate_with_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        generate_files(key, 'files', num_files=value)


def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}'
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        os.rename(f'{directory}/{f}',
                  f'{new_directory}/{f}')


if __name__ == '__main__':
    d = {
        'doc': 2,
        'jpg': 1,
        'png': 3
    }
    generate_with_dictionary(d)
    sort_files('files')