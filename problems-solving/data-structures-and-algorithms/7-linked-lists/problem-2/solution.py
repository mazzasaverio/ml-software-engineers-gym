"""
Problem Statement:

Write a program that takes a singly linked list L 
and two integers s and f as arguments, and reverses 
the order of the nodes from the sth node to 
the fth node, inclusive. The numbering begins at 1, 
where the head node is the first node. Make sure not 
to allocate additional nodes.

Tips: Focus on updating the successor fields.

"""


# Define a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution_1(L, start, finish):
    dummy_head = sublist_head = Node(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            temp,
        )

    return dummy_head.next
