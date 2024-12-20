# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)

for row in matrix:
    print(row, end="\n")
    
print()    

for row in transposed:
    print(row, end="\n")
    
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

# Пример использования
result = create_dict(a=1, b="морковь", c=[3, 4], d={5, 6})
print(result)
# Вывод:
{1: 'a', 'морковь': 'b', '[3, 4]': 'c', '{5, 6}': 'd'}

# 3. Возьмите задачу о банкомате из семинара 2.
# Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти. Сумма пополнения кратна 50 уе. Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 уе.
# После каждой третьей опперации пополнения или снятия начисляются проценты - 3%. Нельзя снять больше, чем на счете. При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией,
# даже ошибочной. Любое действие выводит сумму денег. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


class BankrRobber:
    def __init__(self):
        self.balance = 0
        self.operations = []
        self.operation_count = 0

    def apply_wealth_tax(self):
        if self.balance > 5_000_000:
            tax = self.balance * 0.10
            self.balance -= tax
            print(f"Налог на богатство: {self.format_amount(tax)} уе. Текущий баланс: {self.format_amount(self.balance)} уе.")

    def deposit(self, amount):
        self.apply_wealth_tax()
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 уе.")
            return
        self.balance += amount
        self.operations.append(f"Пополнение: +{self.format_amount(amount)} уе")
        self.operation_count += 1
        if self.operation_count % 3 == 0:
            self.apply_interest()
        print(f"Текущий баланс: {self.format_amount(self.balance)} уе.")

    def withdraw(self, amount):
        self.apply_wealth_tax()
        # if amount % 50 != 0:
        #     print("Сумма снятия должна быть кратна 50 уе.")
        #     return
        fee = max(30, min(600, amount * 0.015))
        print(f"Комиссия за снятие: {self.format_amount(fee)} уе (1.5% от {self.format_amount(amount)} уе)")
        total_withdrawal = amount + fee
        if total_withdrawal > self.balance:
            print("Недостаточно средств на счете.")
            return
        self.balance -= total_withdrawal
        self.operations.append(f"Снятие: -{self.format_amount(amount)} уе (включая комиссию {self.format_amount(fee)} уе)")
        self.operation_count += 1
        if self.operation_count % 3 == 0:
            self.apply_interest()
        print(f"Текущий баланс: {self.format_amount(self.balance)} уе.")

    def apply_interest(self):
        interest = self.balance * 0.03
        self.balance += interest
        self.operations.append(f"Начисление процентов: +{self.format_amount(interest)} уе")
        print(f"Начислены проценты: {self.format_amount(interest)} уе. Текущий баланс: {self.format_amount(self.balance)} уе.")

    def display_operations(self):
        for op in self.operations:
            print(op)

    def show_balance(self):
        print(f"Текущий баланс: {self.format_amount(self.balance)} уе.")

    def exit(self):
        print("Выход из системы.")
        exit()

    def format_amount(self, amount):
        parts = "{:,.2f}".format(amount).split(".")
        parts[0] = parts[0].replace(",", "_")
        return ".".join(parts)

def main():
    account = BankrRobber()
    while True:
        print("\nВыберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Показать все операции")
        print("4. Показать баланс")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            amount = int(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_operations()
        elif choice == '4':
            account.show_balance()
        elif choice == '5':
            account.exit()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
