# EulerTask10 - Сложение простых чисел

# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.

import time


def test_time(function):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = function(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы функции: {dt} сек")
        return res

    return wrapper


def is_simple(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


@test_time
def get_sum(numb):
    s = 0
    for i in range(2, numb):
        if is_simple(i):
            s += i
    return s


print(f"Сумма всех простых чисел меньше десяти: {get_sum(10)}")
print(f"Сумма всех простых чисел меньше двух миллионов: {get_sum(2000000)}")
