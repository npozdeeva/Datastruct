class Node:
    def __init__(self, data=None, link_to_next=None):
        self.data = data
        self.link_to_next = link_to_next

class Stack:
    def __init__(self):
        self.to_next = Node()

    def push(self, data):
        new_node = Node(data)
        new_node.link_to_next = self.to_next
        self.to_next = new_node

    def link_to_next(self):
        return self.link_to_next()

    def to_next(self):
        return self.to_next()

    def data(self):
        return self.data()

    def pop(self):
        remove = self.to_next
        self.to_next = self.to_next.link_to_next
        return remove.data
