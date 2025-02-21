import random
from typing import Union


def add_random(a: int, b: int) -> None:
    """
    Generates two random numbers within the given range and prints their sum.

    Args:
        a (int): The lower bound (inclusive) for random number generation.
        b (int): The upper bound (inclusive) for random number generation.
    """
    number1: int = random.randint(a, b)  # Generate first random number
    number2: int = random.randint(a, b)  # Generate second random number

    print(number1 + number2)  # Print the sum of the two random numbers


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Returns the sum of two numbers.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    # Generate two random numbers for testing
    x: int = random.randint(0, 3)
    y: int = random.randint(3, 10)

    print(x, y)  # Print the randomly generated numbers

    # Call add_random to print the sum of two new random numbers within the given range
    add_random(x, y)
