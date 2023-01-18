"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in numbers]


print(power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_Odd(number):
    return number % 2 > 0


def is_Even(number):
    return number % 2 == 0


def is_Prime(x):
    if x < 2:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return list(filter(is_Odd, numbers))
    elif filter_type == EVEN:
        return list(filter(is_Even, numbers))
    elif filter_type == PRIME:
        return list(filter(is_Prime, numbers))


print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([2, 3, 4, 5], PRIME))