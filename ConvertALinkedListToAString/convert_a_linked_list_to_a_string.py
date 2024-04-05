def stringify(node):
    """
    Convert a linked list represented by nodes into a string.
    """
    output = ''
    while node is not None:
        output += str(node.data) + ' -> '
        node = node.next
    return output + "None"

class Node():
    """
    Class representing a node in a linked list.
    """
    def __init__(self, data, next = None):
        """
        Initialization
        """
        self.data = data
        self.next = next
