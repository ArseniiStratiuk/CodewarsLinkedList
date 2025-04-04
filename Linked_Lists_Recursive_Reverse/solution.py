class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None

def reverse(head: Node | None) -> Node | None:
    def _reverse(node: Node | None, prev: Node | None = None) -> Node | None:
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return _reverse(next_node, node)
    return _reverse(head)
