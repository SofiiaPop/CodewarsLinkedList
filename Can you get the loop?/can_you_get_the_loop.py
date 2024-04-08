def loop_size(node):
    slow = node.next
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = slow.next
    fast = fast.next.next
    i = 1
    while slow != fast:
        i += 1
        slow = slow.next
        fast = fast.next.next
    return i
