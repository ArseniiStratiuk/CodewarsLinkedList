"""Solution for Convert a linked list to a string"""


def stringify(node):
    """Convert a linked list to a string"""
    result = ''
    current = node
    while current:
        result += f'{current.data} -> '
        current = current.next
    result += 'None'
    return result
