import os
os.system("cls")

def summa(x1: int, x2: int) -> int :

    if not (isinstance(x1, int) and isinstance(x2, int) ):
        raise ValueError("На входе должны быть два целых числа!")
    return x1 + x2
print(summa(3,5))
# print(summa._doc_)