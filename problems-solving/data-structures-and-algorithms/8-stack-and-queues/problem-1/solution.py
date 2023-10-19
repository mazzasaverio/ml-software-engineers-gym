"""
Problem Statement:

Consider two singly linked lists, where each node holds a number. 
It is assumed that the lists are sorted, meaning that the numbers 
in each list appear in ascending order. The merge of the two lists 
is a new list that contains the nodes from both lists, with the 
numbers appearing in ascending order. 

"""


# Define a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution_1(L1, L2):
    dummy_head = tail = Node()

    while L1 and L2:
        if L1.val < L2.val:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    while nodes:
        print(nodes.pop())


import collections


class Stack:
    ElementWithCachedMax = collections.namedtuple(
        "ElementWithCachedMax", ("element", "max")
    )

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        return self._element_with_cached_max[-1].max

    def pop(self):
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )
