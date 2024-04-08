class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise TypeError
    new_node = Node(data=source.data)
    new_node.next = dest
    dest = new_node
    source = source.next
    return Context(source, dest)
