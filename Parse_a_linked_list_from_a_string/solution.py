"""Solution for Parse_a_linked_list_from_a_string"""


class Node:
    """Node class for a linked list"""
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


def linked_list_from_string(s):
    """
    Converts a string representation of a linked list into an actual linked list.

    The input string should represent a linked list where nodes are separated by " -> ".
    The last node in the string should be "None" to indicate the end of the list.

    Example:
        Input: "1 -> 2 -> 3 -> None"
        Output: A linked list with nodes containing values 1, 2, and 3.

    Args:
        s (str): A string representation of a linked list.

    Returns:
        Node: The head of the linked list constructed from the input string.
    """
    head = None
    for i in s.split(' -> ')[-2::-1]:
        head = Node(int(i), head)
    return head
