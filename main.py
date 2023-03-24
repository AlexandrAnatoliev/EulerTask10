# EulerTask10 - Сложение простых чисел

# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.

import time


def test_time(function):
    """
    Функция-декоратор, измеряет время выполнения функции function.
    Ждя работы достаточно поставить декоратор "@test_time" перед исследуемой функцией
    :param function: функция, время работы которой измеряется
    :return: Время работы в секундах
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = function(*args, **kwargs)
        finish_time = time.time()
        diff_time = finish_time - start_time
        print(f"Время работы функции: {diff_time} сек")
        return res

    return wrapper


def is_simple(n):
    """
    Функция определяет, является ли число простым
    :param n: число
    :return: True/False
    """
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


@test_time
def get_sum(numb):
    """
    Функция определяет сумму простых чисел до числа numb
    :param numb: максимальное простое число
    :return: сумма простых чисел
    """
    sum_numbers = 0
    for i in range(2, numb):
        if is_simple(i):
            sum_numbers += i
    return sum_numbers


print(f"Сумма всех простых чисел меньше десяти: {get_sum(10)}")
print(f"Сумма всех простых чисел меньше двух миллионов: {get_sum(2000000)}")
