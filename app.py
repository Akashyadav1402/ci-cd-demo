import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)


def is_even(n):
    return n % 2 == 0


def to_upper(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()
