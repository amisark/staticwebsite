from enum import Enum

class TextType(Enum):
    NORMAL="Normal"
    BOLD="Bold"
    ITALIC="Italic"
    CODE="Code"
    LINKS="Links"
    IMAGES="Images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_textnode):
        retcode = False
        if se1f.text == other_textnode.text :
            if self.text_type == other_textnode.text_type :
                if self.url == other_textnode.url :
                    retcode = True
        return(retcode)

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")

