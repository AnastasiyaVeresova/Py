# Задача №31. Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0,
# a1 = 1,
# ak = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


# def fib(n):
#     if n in (0, 1):  # a0 = 0 a1 = 1
#         return n
#     return fib(n - 1) + fib(n - 2)


# print(fib(int(input("Введите номер числа Фибоначчи: "))))




def fib(n):
    if n in (1, 2):
        return n-1
    return fib(n-1)+ fib(n-2)

def str_fib(n):
    res =""
    for i in range(1, n+1):
        res += f'{fib(i)} '
    return res

n= int(input("Введите номер числа Фибоначчи: "))
print(fib(n))
print(str_fib(n))