# Solution for Linked_Lists_Push_BuildOneTwoThree

from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head: 'Node | None', data: int) -> 'Node':
    """
    Create a new Node with the given data and attach it to the front of the linked list.

    Args:
        head (Node | None): The current head of the linked list.
        data (int): The data to store in the new Node.

    Returns:
        Node: The new head of the linked list.
    """
    new = Node(data)
    new.next = head
    return new


def build_one_two_three() -> 'Node':
    """
    Build a linked list with the values 1, 2, and 3.

    Returns:
        Node: The head of the linked list containing the values 1 -> 2 -> 3.
    """
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
