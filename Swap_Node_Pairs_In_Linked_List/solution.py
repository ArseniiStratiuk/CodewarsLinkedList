# Solution for Swap_Node_Pairs_In_Linked_List

class Node:
    """Node class for a linked list"""
    def __init__(self, data = None, next_=None):
        self.data = data
        self.next = next_

def swap_pairs(head: Node):
    dummy = Node()
    dummy.next = head
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return dummy.next
