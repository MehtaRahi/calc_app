# calc_func.py

def add(a, b):
    """Return this sum of a and b."""
    return a + b

def subtract(a, b):
    """Return this difference of a and b."""
    return a - b

def divide(a, b):
    """Return the division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
