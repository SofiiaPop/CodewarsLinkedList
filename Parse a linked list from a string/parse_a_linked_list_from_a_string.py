def linked_list_from_string(s):
    s = s.split(' -> ')
    output = None
    for i in range(len(s)-2, -1, -1):
        output = Node(data=int(s[i]), next=output)
    return output
