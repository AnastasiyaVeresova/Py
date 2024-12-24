# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os

def rename_files(desired_name, num_digits, src_extension, dest_extension, name_range, directory='.'):
    """
    Функция для группового переименования файлов.

    :param desired_name: Желаемое конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param src_extension: Расширение исходного файла.
    :param dest_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени.
    :param directory: Каталог, в котором находятся файлы.
    """
    # Проверяем, что диапазон корректен
    if not (isinstance(name_range, list) and len(name_range) == 2 and all(isinstance(i, int) for i in name_range)):
        raise ValueError("name_range должен быть списком из двух целых чисел")

    start, end = name_range
    if start < 0 or end < 0 or start >= end:
        raise ValueError("name_range должен быть корректным диапазоном")

    # Получаем список файлов в указанном каталоге
    files = [f for f in os.listdir(directory) if f.endswith(src_extension)]

    files.sort()

    # Переименовываем файлы
    for index, filename in enumerate(files):
        # Извлекаем часть оригинального имени
        original_part = filename[start:end]

        # Формируем новое имя файла
        new_name = f"{original_part}{desired_name}{str(index + 1).zfill(num_digits)}.{dest_extension}"

        # Полные пути к старому и новому файлам
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(old_file, new_file)
        print(f"Переименован: {old_file} -> {new_file}")

# Пример использования функции
rename_files(
    desired_name="new_name",
    num_digits=3,
    src_extension="txt",
    dest_extension="txt",
    name_range=[8, 12],
    directory="./"
)
