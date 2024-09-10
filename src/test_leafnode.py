import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_value(self):
        node = LeafNode(value="test")
        self.assertIsNotNone(node)

    @unittest.expectedFailure
    def test_no_children(self):
        child_node = LeafNode(value="test")
        node = LeafNode(children=child_node)
        self.assertIsNotNone(node)

    