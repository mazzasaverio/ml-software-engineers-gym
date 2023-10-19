from solution import solution_1


# Define a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Convert list to linked list
def list_to_linkedlist(lst):
    dummy = Node()
    current = dummy
    for val in lst:
        current.next = Node(val)
        current = current.next
    return dummy.next


# Convert linked list to list
def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


# Tests
def test_empty_lists():
    assert linkedlist_to_list(solution_1(None, None)) == []


def test_one_empty_list():
    l1 = list_to_linkedlist([1, 2, 3])
    assert linkedlist_to_list(solution_1(l1, None)) == [1, 2, 3]


def test_two_sorted_lists():
    l1 = list_to_linkedlist([1, 3, 5])
    l2 = list_to_linkedlist([2, 4, 6])
    assert linkedlist_to_list(solution_1(l1, l2)) == [1, 2, 3, 4, 5, 6]


def test_lists_with_duplicates():
    l1 = list_to_linkedlist([1, 1, 2])
    l2 = list_to_linkedlist([1, 3, 3])
    assert linkedlist_to_list(solution_1(l1, l2)) == [1, 1, 1, 2, 3, 3]
