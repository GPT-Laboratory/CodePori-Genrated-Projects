# calculator.py

import math

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def power(a, b):
    """Returns the result of a raised to the power of b."""
    return a ** b

def modulus(a, b):
    """Returns the remainder when a is divided by b."""
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def factorial(n):
    """Returns the factorial of a number."""
    if n < 0:
        return "Error! Factorial is not defined for negative numbers."
    return math.factorial(n)

def calculator_menu():
    """Displays the available operations in the calculator."""
    print("\n===== Simple Calculator =====")
    print("1) Addition (+)")
    print("2) Subtraction (-)")
    print("3) Multiplication (*)")
    print("4) Division (/)")
    print("5) Power (x^y)")
    print("6) Modulus (%)")
    print("7) Factorial (!)")
    print("8) Exit")
    print("=============================")
