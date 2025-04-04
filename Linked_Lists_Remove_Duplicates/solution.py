# Solution for Linked_Lists_Remove_Duplicates

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head: Node):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
