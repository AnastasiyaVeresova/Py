# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). Ввод: Вывод: 300 220 284

# def sum_of_numbers(n):
#     summa = 0
#     for i in range(1, n):
#         if n % i == 0:
#             summa += i
#     return summa

# n = int(input("Input number: "))
# result = []
# for i in range(n + 1):
#     y = sum_of_numbers(i)
#     #Список делителей для 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — 
#     #их сумма равна 284. мы сделали это
#     if sum_of_numbers(y) == i and i > y:
#         result.append((i, y))
# print(*result)

# print([(i, sum_of_numbers(i)) for i in range(n + 1) if sum_of_numbers(sum_of_numbers(i)) == i and sum_of_numbers(i) > i])

#---------------------------------------

def sum_div(_num_):
    sum = 0
    for i in range(1, _num_ // 2 + 1):
        if _num_ % i == 0:
            sum += i
    return sum

def main():
    user_num = 100001
    while user_num > 100000:
        user_num = int(input("Введите предельное число: "))
        result_list = []
        for i in range(1, user_num):
            sum1 = sum_div(i)
            sum2 = sum_div(sum1)
            if i == sum2 and i != sum1:
                if {sum1, i} in result_list:
                    continue
                result_list.append({sum1, i})
        return result_list

print(main())