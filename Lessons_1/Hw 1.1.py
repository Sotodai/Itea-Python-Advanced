# 1. Написать декоратор, который будет печатать на экран время работы функции.
import time
def timer(func):
    def logic(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print('Time:', time.time() - t)
        return res
    return logic

@timer
def Mul(a, b):
    return a * b

print(Mul(1, 2))
