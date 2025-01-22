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

    def __eq__(textnode1, textnode2):
        retcode = False
        if textnode1.text == textnode2.text :
            if textnode1.text_type == textnode2.text_type :
                if textnode1.url == textnode2.url :
                    retcode = True
        return(retcode)

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")

