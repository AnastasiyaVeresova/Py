# Задача №33. Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



def grades_correction (array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction (array, i - 1, max_num)

array = [1, 3, 3, 3, 4]
grades_correction(array, len(array)-1, max(array))
print(array) #он убирает скобки и запятые
print(*array)


# vas_marks = [1, 3, 3, 3, 4]
# print([min(vas_marks) if i == max(vas_marks) else i for i in vas_marks])


# # ну или так, чтобы метод был:

# vas_marks = [1, 3, 3, 3, 4]

# def reduce_marks(array):
#     return [min(array) if i == max(array) else i for i in array]

# print(reduce_marks(vas_marks))


# def grades_correction (array, i, max_num):
#     if i == -1:
#         return
#     if array[i] == max_num:
#         array[i] = min(array)
#     return grades_correction(array, i - 1, max_num)

# array = [1, 3, 3, 3, 4]
# grades_correction(array, len(array)-1, max(array))

# print(*array)
