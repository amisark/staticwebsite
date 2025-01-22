
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = None
        self.props = None
        if children != None:
            self.children = list(children)
        if props != None:
            self.props    = dict(props)

    def to_html(self):
        raise NotImplementedError(self)

    def props_to_html(self):
        retstrng = ""
        if self.props == None :
            return "None"
        for key in self.props.keys():
            retstrng += f"{key}={self.props[key]} "
        return(retstrng[:-1])
 
    def children_to_string(self):
        retstrng = ""
        if self.children == None:
            return "None"
        for child in children:
            retstrng += f"{child.tag} "
        return retstrng[:-1]



    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children_to_string()}, {self.props_to_html()})")

