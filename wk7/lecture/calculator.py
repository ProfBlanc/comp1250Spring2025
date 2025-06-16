import math
import string
import random

# print(math.pi)
# print(string.ascii_lowercase)
# print(math.floor(1.999))
print(string.capwords("prof ben blanc", " "))

"""
Officially describe this module. What it does, how it behaves, etc
"""


allowed_operations = "+,-,*,**,/,//,%".split(",")


def add(n1: float | int, n2: int | float) -> int | float:
    """
    Perform addition operation on two numbers
    :param n1: first of two numbers
    :param n2: second of two numbers
    :type n1 float|int
    :type n2 float|int
    :return: the sum of the two numbers

    >>> add(5, 10)
    15
    >>> add(5.5, 10.10)
    15.6
    >>> add(5, 1.1)
    6.1
    >>> add(2.2, 3)
    5.2

    """
    return round(n1 + n2, 5)


def calculate(n1, operator, n2):
    """
    >>> calculate('1', 345.34, 943)
    'not implemented'
    >>> calculate(23320, "345.34", True)
    'not implemented'

    """
    return "not implemented"


def test_func1():
    """
    >>> test_func1()
    ['hi', 123, 98.76]
    """
    return ["hi", 123, 98.76]

def test_func2():
    """
    >>> test_func2()
    {'name': 'comp1250', 'mark': 100}

    """
    return {"name": "comp1250", "mark": 100}
