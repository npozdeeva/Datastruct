from unittest import TestCase
from classes import Stack


class TestClass(TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_data(self):
        self.assertEqual(self.stack.to_next.data, 'data3')
        self.assertEqual(self.stack.to_next.link_to_next.data, 'data2')
        self.assertEqual(self.stack.to_next.link_to_next.link_to_next.data, 'data1')

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'data3')