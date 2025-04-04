"""Solution for moving a node from one linked list to another."""


class Node:
    def __init__(self, data: int) -> None:
        """
        Initialize a Node with data and a pointer to the next node.
        :param data: The data value of the node.
        """
        self.data: int = data
        self.next: Node = None


class Context:
    def __init__(self, source: Node, dest: Node) -> None:
        """
        Initialize a Context object with source and destination linked lists.
        :param source: The source linked list.
        :param dest: The destination linked list.
        """
        self.source: Node = source
        self.dest: Node = dest


def move_node(source: Node, dest: Node) -> Context:
    """
    Move the head node from the source linked list to the destination linked list.
    :param source: The source linked list.
    :param dest: The destination linked list.
    :return: A Context object containing the updated source and destination lists.
    :raises Exception: If the source linked list is empty.
    """
    if source is None:
        raise Exception("Source linked list is empty.")

    dest_new = Node(source.data)
    source = source.next
    dest_new.next = dest

    return Context(source, dest_new)
