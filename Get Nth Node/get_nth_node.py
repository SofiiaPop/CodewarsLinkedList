from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    """
    Get Nth Node
    """
    if index < 0 or node is None:
        raise TypeError
    for i in range(index):
        node = node.next
        if node.next == None and i != index - 1:
            raise TypeError
    return node
