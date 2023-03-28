from unittest import TestCase
from classes import Stack
from custom_queue import Queue


class TestClass(TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_data(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.link_to_next.data, 'data2')
        self.assertEqual(self.stack.top.link_to_next.link_to_next.data, 'data1')

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'data3')

class TestQuene(TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.link_to_next.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.link_to_next, None)