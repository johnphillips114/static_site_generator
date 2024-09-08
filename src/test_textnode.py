import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://google.ca")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold", "https://google.ca")
        node2 = TextNode("This is a text node", "italic", "https://google.ca")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a different text node", "bold", "https://google.ca")
        node2 = TextNode("This is a text node", "bold", "https://google.ca")
        self.assertNotEqual(node, node2)
    
    @unittest.expectedFailure
    def test_no_url(self):
        node = TextNode("This node has no url", "bold")

    @unittest.expectedFailure
    def test_no_text_type(self):
        node = TextNode(text = "This node has no url", url = "https://boot.dev")

    @unittest.expectedFailure
    def test_no_text(self):
        node = TextNode(text_type = "This node has no url", url = "https://boot.dev")


if __name__ == "__main__":
    unittest.main()
