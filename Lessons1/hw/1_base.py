# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. # Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Треугольник существует и является равносторонним"
        if a == b or a == c or b == c:
            return "Треугольник существует и является равнобедренным"
        else: return "Треугольник существует и является разносторонним"
    else: return "Треугольник не существует"
    
a = 3
b = 3
c = 3

print(check_triangle(a, b, c))

# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_number():
    while True:
        try:
            num = int(input("Введите число от 0 до 100 000: "))
            if num < 0 or num > 100000:
                print("Число должно быть в диапазоне от 0 до 100 000")
            else:
                break
        except ValueError:
            print("Некорректный ввод. Введите целое число")

    if num == 0 or num == 1:
        print(f"Число {num} не является ни простым, ни составным")
    elif is_prime(num):
        print(f"Число {num} является простым")
    else:
        print(f"Число {num} является составным")

check_number()

# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

def user_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 10
    print("Угадайте число от 1 до 1000 за 10 попыток")

    for attempt in range(attempts):
        try:
            user_guess = int(input(f"Попытка {attempt + 1}: Ведите предполагаемое число: "))
            if (user_guess < LOWER_LIMIT or user_guess > UPPER_LIMIT):
                print ("Число должно быть в диапазоне 0 - 1 000")
                continue
            if user_guess < num:
                print("Больше")
            elif user_guess > num:
                print("Меньше")
            else:
                print(f"Мои поздравления! Вы угадали число {num} с {attempt + 1} попытки")
                break
        except ValueError:
            print("Некорректный ввод. Пожалуйста введите целое число")
    else:
        print(f"Вы не угадали число - было загадано {num}")

user_number()







