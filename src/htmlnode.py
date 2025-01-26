
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
        for child in self.children:
            retstrng += f"{child.tag} "
        return retstrng[:-1]



    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children_to_string()}, {self.props_to_html()})")

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("value unspecified")

        props_str = ""
        if self.props :
            for key in self.props.keys():
                props_str += f" {key}={self.props[key]}"

        ret_str = ""
        if not self.tag :
            ret_str = f"{props_str[1:]} {self.value}"
        else:
            ret_str += f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        return ret_str


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        props_str = ""
        if self.props :
            for key in self.props.keys():
                props_str += f" {key}={self.props[key]}"

        ret_str = ""
        if not self.tag :
            raise Exception("empty tag in ParentMode")
    
        ret_str += f"<{self.tag}{props_str}>"

        children_str = ""
        if self.children :
            children_str += ParentNode.get_children_str(self.children)

        ret_str += f"{children_str}</{self.tag}>"
        return ret_str

    def get_children_str(children):
        child_str = ""
        for child in children:
            if child.tag != None :
                props_str = child.props_to_html()
                child_str += f"<{child.tag} {props_str}>"
            if child.children:
                child_str += ParentNode.get_children_str(child.children)
            if child.value :
                child_str += f"{child.value}"
            if child.tag != None :
                child_str += f"</{child.tag}>"
        return child_str
        
