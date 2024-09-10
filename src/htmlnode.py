

class HTMLNode:
    def __init__(self):
        self.tag = None
        self.value = None
        self.children = None
        self.props = None

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html_string = " "
        for prop in self.props:
            html_string += f"{prop}=\"{self.props[prop]}\""
        return html_string
    
    def __repr__(self):
        self_string = "--- HTMLNode ---"
        if self.tag != None:
            self_string += f"\n\tTag: {self.tag}"
        if self.value != None:
            self_string += f"\n\tValue: {self.value}"
        if self.children != None:
            self_string += f"\n\tChildren: {self.children}"
        if self.props != None:
            self_string += f"\n\tProps: {self.props}"