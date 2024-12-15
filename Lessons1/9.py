rows = int(input("Ввежите количество рядов для ёлочки: "))
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
