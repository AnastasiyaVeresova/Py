def f(x):
    return x*x
a = f
print(f(5))
print(a(5))

____________________________________________________________________миникалькулятор

def calc1(a, b):
    return a + b
    
def calc2(a, b):
    return a * b
    
def math(op, x, y):
    print(op(x, y))
    
math(calc2, 5, 7)

-------------------------------------

# calc1 = lambda a,b: a + b
    
math(lambda a,b: a + b, 5, 7)
