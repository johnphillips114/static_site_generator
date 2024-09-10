import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_blank_repr(self):
        node = HTMLNode()
        self.assertIsNotNone(node)

    def test_props_to_html(self):
        node = HTMLNode()
        props = {}
        props["href"] = "https://google.com"
        props["target"] = "_blank"
        node.props = props
        self.assertIsNotNone(node.props_to_html())