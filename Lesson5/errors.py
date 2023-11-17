'''def print_operation_table(operation, num_columns, num_rows):
    if num_rows < 2 and num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_columns + 1):
            for j in range(1, num_rows + 1):
                if operation(j, i) == j + i:
                    print(value := operation(i, j), end=' ')
            print()


# def print_operation_table(operation, num_columns, num_rows):
#     if num_rows < 2 and num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         value = [[operation(i, j) for j in range(1, num_rows + 1)] for i in range(1, num_columns + 1)]
#         for i in value:
#             print(*[f"{x}" for x in i])
#         print()

print_operation_table(lambda x, y: x + y, 4, 4)

# Ожидаемый ответ:

# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

# Ваш ответ:

# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8
print_operation_table(lambda x, y: x - y, 5, 5)

# Ожидаемый ответ:

# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0

# Ваш ответ:

# 0 1 2 3 4
# -1 0 1 2 3
# -2 -1 0 1 2
# -3 -2 -1 0 1
# -4 -3 -2 -1 0
print_operation_table(lambda x, y: x / y, 4, 4)

# Ожидаемый ответ:

# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0

# Ваш ответ:

# 1.0 2.0 3.0 4.0
# 0.5 1.0 1.5 2.0
# 0.3333333333333333 0.6666666666666666 1.0 1.3333333333333333
# 0.25 0.5 0.75 1.0

print_operation_table(lambda x, y: x * y, 1, 2)
# Ожидаемый ответ:

# ОШИБКА! Размерности таблицы должны быть больше 2!

# Ваш ответ:

# 1 2'''


