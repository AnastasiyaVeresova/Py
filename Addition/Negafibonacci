#Задача НЕГАФИБОНАЧЧИ
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:

#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

fib1 = 1
fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
result = []
for i in range(n):
    if i >= 0:
        fib_sum = fib1 + fib2
        fib1 = fib2
        result.append(fib2)
        fib2 = fib_sum
        i = i + 1
result.reverse()
print(result)        
print(f'Число Фибоначчи для {n} =', fib_sum)

fib1 = result[0]
fib2 = result[1]
res = []

for i in range(17):
    fib_diff = fib1 - fib2
    fib1 = fib2
    res.append(fib2)
    fib2 = fib_diff
    i = i + 1
res.reverse()     
print(f'{res} [Негафибоначчи]')
  
