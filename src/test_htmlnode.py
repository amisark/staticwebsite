import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html1(self):
        node1 = HTMLNode("p", "test paragraph")
        node2 = HTMLNode("p", "test paragraph")
        node1str = node1.__repr__()
        node2str = node2.__repr__()
        self.assertEqual(node1str, node2str)

    def test_html2(self):
        node1 = HTMLNode("p", "test paragraph", None)
        node2 = HTMLNode("p", "test paragraph")
        node1str = node1.__repr__()
        node2str = node2.__repr__()
        print(f">{node1str}<")
        print(f">{node2str}<")
        self.assertEqual(node1str, node2str)
    
    def test_html3(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        tststr = "href=https://www.google.com target=_blank"
        node1 = HTMLNode("p", "test paragraph", None, props)
        props_str = node1.props_to_html()
        self.assertEqual(props_str, tststr)
        
    def test_html4(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode("p", "test paragraph", None, props)
        node2 = HTMLNode("p", "test paragraph", None)
        node1str = node1.__repr__()
        node2str = node2.__repr__()
        print(f">{node1str}<")
        print(f">{node2str}<")
        self.assertNotEqual(node1str, node2str)
    

if __name__ == "__main__":
    unittest.main()
