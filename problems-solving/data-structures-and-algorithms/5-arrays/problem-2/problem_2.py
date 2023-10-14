"""
Problem Statement:

Write a program that takes an array of digits representing a non-negative decimal integer,
D, as input and updates the array to represent the integer D + 1. The array represents the 
integer with each element being a digit and the most significant digit appearing first.

For example, if the input is [7, 2, 9], the array should be updated to [7, 3, 0] since 729 + 1 = 730.

The algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

Example:
    If the input is [7, 2, 9], your function should update the array to [7, 3, 0].

"""


def plus_one_1(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    print(A)


def plus_one_2(A):
    print("Input: ", A)
    report = 0
    for i in reversed(range(len(A))):
        if A[i] == 9:
            report = 1
            A[i] = 0
        else:
            A[i] = A[i] + report
            if A[i] == 10:
                report = 1
                A[i] = 0
            else:
                break

    print("Output: ", A)


plus_one_1([1, 2, 9])
