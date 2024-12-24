def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def process_files(file_numbers, file_names, file_res):
    with open(file_numbers, 'r', encoding='utf-8') as f_num:
        with open(file_names, 'r', encoding='utf-8') as f_name:
            with open(file_res, 'w', encoding='utf-8') as f_res:
                # Читаем все строки, чтобы определить длину файлов
                lines_num = f_num.readlines()
                lines_name = f_name.readlines()
                length1 = len(lines_num)
                length2 = len(lines_name)
                length = max(length1, length2)
                

                # Возвращаем указатель в начало файлов
                f_num.seek(0)
                f_name.seek(0)

                for i in range(length):
                    line_num = read_line_or_begin(f_num)
                    line_name = read_line_or_begin(f_name)
                    if line_num and line_name:
                        a, b = line_num.split('|')
                        a = int(a)
                        b = float(b)
                        res = a * b
                        if res < 0:
                            res *= -1
                            line_name = line_name.lower()
                        else:
                            res = round(res)
                            line_name = line_name.upper()
                        f_res.write(f'{line_name} {res}')
                        f_res.write('\n' if i < length - 1 else "")

if __name__ == '__main__':
    process_files('data.txt', 'data_names.txt', 'f_res.txt')
