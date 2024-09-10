from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value):
        super().__init__(self)
        self.tag = None
        self.value = value
        self.props = None

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node doesn't have a value")
        if self.tag == None:
            return self.value
        html_string = f"<{self.tag}"
        if self.props != None:
            html_string += self.props_to_html()
        html_string += f">{self.value}</{self.tag}>"
