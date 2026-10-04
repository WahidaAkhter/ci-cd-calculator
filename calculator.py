def add(a: float | int, b: float | int) -> float | int:
    return a + b  # Return the sum to the caller.


def subtract(a: float | int, b: float | int) -> float | int:
    return a - b  # Return the difference to the caller.


def multiply(a: float | int, b: float | int) -> float | int:
    return a * b  # Return the product to the caller.


def divide(a: float | int, b: float | int) -> float | int:
    # Student exercise: enable the zero-division test, observe
    if b == 0:  # Detect a denominator for which division is
        raise ValueError("Cannot divide by zero.")  # Report
    return a / b  # Return a floating-point quotient for a vali


def power(base: float | int, exponent: int) -> float | int:
    if base == 0 and exponent < 0:
        raise ValueError("Zero cannot have a negative exponent")
    return base ** exponent