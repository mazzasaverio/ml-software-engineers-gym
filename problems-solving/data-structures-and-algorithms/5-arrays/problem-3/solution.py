"""
Problem Statement:

Certain applications require arbitrary precision arithmetic. One way to achieve this
is to use arrays to represent integers. Each array entry represents a digit, with the
most significant digit appearing first. A negative leading digit denotes a negative integer.

For example, the sequence [1, 9, 3, 7, 0, 7, 7, 2, 1] represents the number 193707721, and
the sequence [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7] represents the number -761838257287.

The task is to write a program that takes two arrays representing integers and returns
an integer representing their product.

Example:
    If the inputs are [1, 9, 3, 7, 0, 7, 7, 2, 1] and [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7],
    your function should return [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7],
    since 193707721 * -761838257287 = -147573952589676412927.

"""


def solution(num1, num2):
    # Determine the sign of the result
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1

    # Take the absolute value of the first digit (which could be negative)
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # Initialize the result list with zeros
    result = [0] * (len(num1) + len(num2))

    # Multiply each digit of num1 with each digit of num2
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes
    result = result[
        next((i for i, x in enumerate(result) if x != 0), len(result)) :
    ] or [0]

    # Apply the sign to the result
    return [sign * result[0]] + result[1:]
