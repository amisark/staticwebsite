import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    

    def test_leaf1(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        tststr = "href=https://www.google.com target=_blank"
        node1 = LeafNode("p", "test paragraph", props)
        node2 = LeafNode("p", "test paragraph", props)
        leaf1str = node1.to_html()
        leaf2str = node2.to_html()
        print(leaf1str)
        self.assertEqual(leaf1str, leaf2str)

    def test_leaf2(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        tststr = "href=https://www.google.com target=_blank"
        node1 = LeafNode("p", "test paragraph", props)
        leaf1str = node1.to_html()
        leafstr_expected = "<p href=https://www.google.com target=_blank>test paragraph</p>"
        self.assertEqual(leaf1str, leafstr_expected)


    def test_leaf3(self):
        node1 = LeafNode("p", "test paragraph")
        node2 = LeafNode("p", "test paragraph")
        leaf1str = node1.to_html()
        leaf2str = node2.to_html()
        print(leaf1str)
        self.assertEqual(leaf1str, leaf2str)

    def test_leaf3(self):
        node1 = LeafNode("p", "")
        self.assertRaises(SystemExit)

    def test_leaf4(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        tststr = "href=https://www.google.com target=_blank"
        node1 = LeafNode("", "test paragraph", props)
        leaf1str = node1.to_html()
        leafstr_expected = "href=https://www.google.com target=_blank test paragraph"
        self.assertEqual(leaf1str, leafstr_expected)

    def test_parentmode1(self):
        tag = "p"
        props = None
        children = [ LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text") ]
        node1 = ParentNode(tag, children, props)
        print(f"pn {node1.to_html()}")

    def test_parentmode2(self):
        tag = "p"
        props = None
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        children2 = [
            HTMLNode("a", "level 2", None, props1 ),
            LeafNode("i", "italic text")
        ]
        children = [ LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            HTMLNode("a", "click here", None, props1 ),
            LeafNode(None, "Normal text"),
            LeafNode("a", "click here REALLY", props1 ),
            HTMLNode("a", "click here", None, props1 ) ]
        node1 = ParentNode(tag, children, props)
        expected_str = "<p><b None>Bold text</b>Normal text<a href=https://www.google.com target=_blank>click here</a>Normal text<a href=https://www.google.com target=_blank>click here REALLY</a><a href=https://www.google.com target=_blank>click here</a></p>"
        #print(f"pn2 {node1.to_html()}")
        self.assertEqual(node1.to_html(), expected_str)

    def test_parentmode3(self):
        tag = "p"
        props = None
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        children2 = [
            HTMLNode("a", "level 2", None, props1 ),
            LeafNode("i", "italic text")
        ]
        children = [ LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            HTMLNode("a", "click here", None, props1 ),
            LeafNode(None, "Normal text"),
            LeafNode("a", "click here REALLY", props1 ),
            HTMLNode("a", "click here", children2, props1 ) ]
        node1 = ParentNode(tag, children, props)
        expected_str="<p><b None>Bold text</b>Normal text<a href=https://www.google.com target=_blank>click here</a>Normal text<a href=https://www.google.com target=_blank>click here REALLY</a><a href=https://www.google.com target=_blank><a href=https://www.google.com target=_blank>level 2</a><i None>italic text</i>click here</a></p>"
        #print(f"pn3 {node1.to_html()}")
        self.assertEqual(node1.to_html(), expected_str)
if __name__ == "__main__":
    unittest.main()
