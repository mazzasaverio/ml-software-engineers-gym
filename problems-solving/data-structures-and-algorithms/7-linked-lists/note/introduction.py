
class Node:
    def __init__(self, data):
        self.data = data  # The data contained in the node
        self.next = None  # The reference to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """ Append a new node with the provided data to the end of the list """
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def print_list(self):
        """ Print all the nodes in the list """
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()