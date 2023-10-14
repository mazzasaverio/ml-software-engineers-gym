# Write a program that takes an array of digits representing a non-negative decimal integer,
# D, as input and updates the array to represent the integer D + 1. For example, if
# the input is (7, 2, 9), the array should be updated to (1, 3, 0). Your algorithm
# should work even if it is implemented in a
# language that has finite-precision arithmetic.


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
