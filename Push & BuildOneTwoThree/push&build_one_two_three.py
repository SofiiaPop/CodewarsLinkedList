from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    node = Node(data=data)
    node.next = head
    return node

def build_one_two_three():
    node1 = None
    node2 = Node(3)
    node2.next = node1
    node3 = Node(2)
    node3.next = node2
    node4 = Node(1)
    node4.next = node3
    return node4
