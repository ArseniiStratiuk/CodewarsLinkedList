"""
Solution for Get_nth_node_in_a_linked_list
"""


class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node: Node, index: int) -> Node:
    """
    Retrieves the nth node (0-based index) from a linked list.

    Args:
        node (Node): The head node of the linked list.
        index (int): The 0-based index of the node to retrieve.

    Returns:
        Node: The node at the specified index.

    Raises:
        Exception: If the index is out of bounds or the list is empty.
    """
    count = 0
    while True:
        if node is None:
            raise Exception("Index out of bounds.")
        if count == index:
            return node
        node = node.next
        count += 1
