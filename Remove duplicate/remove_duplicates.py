class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    while current:
        while current.next and current.data == current.next.data:
            current.next = current.next.next
        current = current.next
    return head
