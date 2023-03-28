from classes import Node, Stack
from custom_queue import Queue

# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# print(n2.link_to_next)
#
# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# stack.push('data3')
# print(stack.top.data)
# print(stack.top.link_to_next.data)
# print(stack.top.link_to_next.link_to_next.data)
# print(stack.top.link_to_next.link_to_next.link_to_next)
# print(stack.top.link_to_next.link_to_next.link_to_next.data)
#
#
# ####
# print("Task2:")
# stack = Stack()
# stack.push('data1')
# data = stack.pop()
#
# # стэк стал пустой
# print(stack.top)
#
#
# # pop() удаляет элемент и возвращает данные удаленного элемента
# print(data)
#
# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# data = stack.pop()
#
# # теперь последний элемента содержит данные data1
# print(stack.top.data)
#
#
# # данные удаленного элемента
# print(data)

print("Task3:")
queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.head.data)
print(queue.head.link_to_next.data)
print(queue.tail.data)
print(queue.tail.link_to_next)
print(queue.tail.link_to_next.data)