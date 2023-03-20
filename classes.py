class Node:
    def __init__(self, data, link_to_next=None):
        self.data = data
        self.link_to_next = link_to_next

class Stack:
    def __init__(self):
        self.to_next = None

    def push(self, data):
        new_node = Node(data)
        new_node.link_to_next = self.to_next
        self.to_next = new_node


# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)