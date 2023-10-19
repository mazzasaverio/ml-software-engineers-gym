"""
Problem Statement:

Although a linked list is intended to be a sequence of nodes ending in null,
it is possible to create a cycle in a linked list by making the next field of 
an element reference one of the earlier nodes.

Write a program that takes the head of a singly linked list. If there
is no cycle, the program should return null. If a cycle is present, 
the program should return the node at the start of the cycle. Note 
that the length of the list is not known in advance.

"""


# Define a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution_1(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None
