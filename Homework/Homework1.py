# Homework problem number 1


def fibfor(n):
    """N describes the nth term of the fibonacci sequence"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a = 0
    b = 1
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    return c

# Homework problem number 2

def goldenratio(x):
    return fibfor(x-1)/fibfor(x)

# Homework problem number 3

import math
def math_golden_ratio():
    """prints the golden ratio using the math module"""

    print((math.sqrt(5) - 1)/2)


# [Bonus] Homework problem number 4

def superbigscientificnotation(n, accuracy=2):
    string_num = str(n)
    first = string_num[:1]
    otherdigits = int(string_num[1:accuracy + 2]) + 5
    otherdigits = str(otherdigits)
    otherdigits = otherdigits[:len(otherdigits) - 1]
    scientific_pt1 = first + '.' + otherdigits
    number_of_tens = int(math.log(n, 10))
    second_part = 'e+' + str(number_of_tens)
    return scientific_pt1 + second_part
