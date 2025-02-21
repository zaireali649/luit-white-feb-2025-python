import random


def add_random(a, b):
    number1 = random.randint(a, b)
    number2 = random.randint(a, b)

    print(number1 + number2)

def add(a, b):
    return a + b

if __name__=="__main__":

    x = random.randint(0, 3)
    y = random.randint(3, 10)

    print(x, y)
    add_random(x, y)