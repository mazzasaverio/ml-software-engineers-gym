# Write a method that takes a sorted array and a key, and returns the index of the
# first occurrence of that key in the array.


def solution_1(A, key):
    for index, value in enumerate(A):
        if A[index] == key:
            return index

    return -1


def solution_2(A, key):
    left, right, result = 0, len(A) - 1, -1

    while left <= right:
        mid = left + (right - left) // 2

        if A[mid] > key:
            right = mid - 1
        elif A[mid] == key:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
