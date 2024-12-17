# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def int_to_hex(n):
    if n == 0:
        return "0x0"
    hex_chars = "0123456789abcdef"
    hex_str = ""
    while n > 0:
        hex_str = hex_chars[n % 16] + hex_str
        n //= 16
    return "0x" + hex_str

number = 255
print(int_to_hex(number))  # Вывод: 0xff
print(hex(number))  # Проверка: 0xff

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def add_fractions(frac1, frac2):
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))
    sum_fraction = Fraction(num1, denom1) + Fraction(num2, denom2)
    return sum_fraction

def multiply_fractions(frac1, frac2):
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))
    product_fraction = Fraction(num1, denom1) * Fraction(num2, denom2)
    return product_fraction

frac1 = "1/2"
frac2 = "3/2"

sum_result = add_fractions(frac1, frac2)
product_result = multiply_fractions(frac1, frac2)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")


