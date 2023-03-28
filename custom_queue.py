class Node:
    def __init__(self, data=None, link_to_next=None):
        self.data = data
        self.link_to_next = link_to_next


class Queue:
    def __init__(self, start=None, head=None):
        self.start = start
        self.head = head

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.link_to_next = new_node
            self.tail = new_node


# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
#
# print(queue.head.data)
# print(queue.head.link_to_next.data)
# print(queue.tail.data)
# print(queue.tail.link_to_next)
# print(queue.tail.link_to_next.data)