# Imagine you're given an array A and an index i into A. The goal is to rearrange
# the elements such that all elements less than A[i] (the "pivot") appear first,
# followed by elements equal to the pivot, and then elements greater than the pivot.


def dutch_flag_partition(pivot_index, A):
    print(f"pivot_index: {pivot_index}")
    print(f"A: {A}")
    pivot = A[pivot_index]

    print("First pass: group elements smaller than pivot.")
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            print(f"A[i]: {A[i]} - A[j]: {A[j]} - pivot: {pivot}")
            if A[j] < pivot:
                print(f"condition - A[j]: {A[j]} - pivot: {pivot}")
                A[i], A[j] = A[j], A[i]
                print(A)
                break

    print("Second pass: group elements larger than pivot.")
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        print(j, i)
        for j in reversed(range(i)):
            print(f"- {j}")
            print(f"i:{i} - j:{j} #### A[j]: {A[j]} - pivot: {pivot}")
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    print(f"A final: {A}")


# Test the function
dutch_flag_partition(2, [3, 1, 2, 1, 1, 4])
