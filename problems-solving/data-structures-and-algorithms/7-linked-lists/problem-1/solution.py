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
