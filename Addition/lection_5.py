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

___________________________________________________
data = [1, 2, 3, 5, 8, 15, 23, 38]
result = []

for i in data:
    if i % 2 == 0:
        result.append((i, i**2))

print(result)

# [(2, 4), (8, 64), (38, 1444)]
________________________________________________lambda function

def select(f, col):
    return [f(x) for x in col]
    
def where(f, col):
    return [x for x in col if f(x)]
    
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)

#[1, 2, 3, 5, 8, 15, 23, 38]
#[2, 8, 38]
________________________________________________________


def select(f, col):
    return [f(x) for x in col]
    
def where(f, col):
    return [x for x in col if f(x)]
    
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]

-------------------------------------------------

def where(f, col):
    return [x for x in col if f(x)]
    
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = where(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]


