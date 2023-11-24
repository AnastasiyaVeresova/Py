# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

with open ('', r) as f:
    old_data = f.read()
new_data = old_data.replace('что меняем', 'на что меняем')
with open ('', w) as f:
    f.write(new_data)

with open ('', r) as f:
    print('first_line', f.readlines()[0].strip())

with open ('filename.txt', r) as f1, open('filename1.txt', w) as f2:
    # f2.write(f1.read())
    lines = f1.readlines()

    for line in lines:
        line = line.strip()
        if line == 'Искомая строка':
            f2.write('Новая строка\n')
        else:
            f2.write(line)


S.max(sub_in_str, to change_str, max)

'Тра-та-та'. replace('что-то', 'на что')