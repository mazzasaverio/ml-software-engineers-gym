"""
This problem is concerned with deleting repeated elements from a sorted array. For example, given the array <2,3,5,5,7,11,11,77,73>, after deletion, the array should be (2,3,5,7,77,73,0,0,0). After deleting repeated elements, there are 6 valid entries. There are no requirements for the values stored beyond the last valid element.

Write a program that takes a sorted array as input and updates it so that all duplicates are removed. The remaining elements should be shifted left to fill the emptied indices. Return the number of valid elements. Note that you cannot use library functions that perform this operation.

Hint: There is an O(n) time and O(1) space solution.
"""


def delete_duplicates(A):
    A_new = []
    for x in A:
        print(x)
        if x not in A_new:
            print(x)
            A_new.append(x)

            print(A_new)

    return A_new


delete_duplicates([2, 3, 5, 5, 7, 11, 11, 77, 73])
