"""
Problem Statement:

Imagine you're given an array A and an index i into A. The goal is to rearrange the elements
such that all elements less than A[i] (the "pivot") appear first, followed by elements equal
to the pivot, and then elements greater than the pivot.

The task is to write a program that takes an array and an index as input and rearranges the array
according to the above-mentioned conditions.

Example:
    Given array A = [4, 9, 6, 8, 2, 7] and index i = 2 (A[i] = 6),
    after rearrangement, the array should look something like [4, 2, 6, 9, 8, 7].

Note: The elements can appear in any order within their respective group (i.e., less than, 
equal to, or greater than the pivot).

"""


def dutch_flag_partition_1(pivot_index, A):
    pivot = A[pivot_index]

    print("First pass: group elements smaller than pivot.")
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    print("Second pass: group elements larger than pivot.")
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition_2(pivot_index, A):
    pivot = A[pivot_index]

    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def dutch_flag_partition_3(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    # Keep iterating as long as there is an unclassified element.

    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# Test the function
dutch_flag_partition_3(2, [3, 1, 2, 1, 1, 4])
