class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise TypeError
    if not head or not head.next:
        return Context(head, None)

    first_head = head
    second_head = head.next

    current = head
    next_node = head.next

    while current and next_node:
        current.next = next_node.next
        current = current.next
        if current:
            next_node.next = current.next
            next_node = next_node.next

    if current:
        current.next = None

    return Context(first_head, second_head)
