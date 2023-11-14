# Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
import os
os.system("cls")
def recursion_expression(expression):
    if len(expression) == 1:
        return int(expression[0])
    else:
        operator = expression[1]
        operand_one = int(expression[0])
        operand_two = int(recursion_expression(expression[2:]))
        if operator == '+':
            return operand_one + operand_two
        elif operator == '-':
            return operand_one - operand_two
        elif operator == '/':
            return operand_one/operand_two
        elif operator == '*':
            return operand_one*operand_two
        
expression = input('Введите выражение для вычисления: ')
result = recursion_expression(expression.split())
print(f'Ответ', result)



