# 3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму наибольших двух из них.
def func(a, b, c):
    if(a + b >= a + c >= b + c):
        return a + b
    else:
        if(a + c >= b + c):
            return a + c
        else:
            return b + c

print(func(1, 2, 4))