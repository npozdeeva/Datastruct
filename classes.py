class Node:
    def __init__(self, data=None, link_to_next=None):
        self.data = data
        self.link_to_next = link_to_next

class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, data):
        new_node = Node(data)
        new_node.link_to_next = self.top
        self.top = new_node

    def link_to_next(self):
        return self.link_to_next()

    def to_next(self):
        return self.top()

    # def data(self):
    #     return self.data()

    def pop(self):
        remove = self.top
        self.top = self.top.link_to_next
        return remove.data
