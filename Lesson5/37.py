# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Input:    2 -> 3 4 Output: 4 3




# ????????????--------------------
# def reverse(n, arr):
#     if n < 1:
#         return
#     print(arr[n-1])
#     reverse(n-1,arr)



# num = 5

# def reverse_output(n, x = None):
#     if n > 0:
#         x = input("Введите число: ")
#         reverse_output(n - 1)
#     if x != None:
#         print(x, end=" ")

# reverse_output(num)



# def reverse_num(n, numbers):
#     if n == 0:
#         return
#     print(numbers[n-1], end= " ")
#     return reverse_num(n-1, numbers)

# reverse_num(4, [1, 3, 4, 5])


def rec(n):
    if n == 0:
        return ''
    x = int(input("Введите число: "))
    return rec(n - 1) + f' {x}'


n = int(input("Введите кол-во чисел: "))
print(rec(n))