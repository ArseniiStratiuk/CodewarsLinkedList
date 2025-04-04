"""Solution for inserting a node into a sorted linked list."""


class Node:
    def __init__(self, data: int) -> None:
        """
        Initialize a Node with data and a pointer to the next node.
        
        :param data: The integer value to store in the node.
        """
        self.data: int = data
        self.next: Node = None


def sorted_insert(head: Node, data: int) -> Node:
    """
    Insert a new node with the given data into the sorted linked list.

    :param head: The head of the sorted linked list.
    :param data: The integer value to insert into the list.
    :return: The head of the updated linked list.
    """
    new = Node(data)
    if head is None:
        return new
    curr = head
    if curr.data >= data:
        new.next = head
        return new
    while True:
        if curr.data < data and (curr.next is None or curr.next.data > data):
            new.next = curr.next
            curr.next = new
            return head
        curr = curr.next
