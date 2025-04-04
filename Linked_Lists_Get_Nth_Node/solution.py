# Solution for Linked_Lists_Get_Nth_Node

from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    count = 0
    while True:
        if node is None:
            raise Exception
        if count == index:
            return node
        node = node.next
        count +=1
