from textnode import *


def main():
    print("Hello World!")
    textnode = TextNode("This is a text node", TextType.BOLD, "dummyurl")
    print(textnode.__repr__())

if __name__ == "__main__":
    main()

