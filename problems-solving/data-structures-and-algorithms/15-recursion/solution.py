def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide the list in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Traverse through both left and right lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any leftovers. Since we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # elements are already sorted.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
