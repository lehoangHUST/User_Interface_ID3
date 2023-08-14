from lxml import etree
import graphviz

def tree_to_xml(node):
    if node.label is None:
        element = etree.Element(str(node.split_attribute))
    else:
        element = etree.Element(str(node.label))

    for edge_i, child in enumerate(node.children):
        child_element = tree_to_xml(child)
        if len(node.children):
            child_element.set("edge_name", str(node.order[edge_i]))
        element.append(child_element)
    return element


def object_tree_to_xml_string(root):
    root_element = tree_to_xml(root)
    xml_string = etree.tostring(root_element, pretty_print=True, encoding="UTF-8")
    return xml_string


def xml_to_dot(xml_element, parent=None):
    dot_code = ''
    node_label = xml_element.tag
    node_id = node_label.replace(' ', '_')
    
    if parent is not None:
        edge_name = xml_element.get("edge_name", "")
        dot_code += f'\t"{parent}" -> "{node_id}" [label="{edge_name}"];\n'
        
    dot_code += f'\t"{node_id}" [label="{node_label}"];\n'
    
    for child in xml_element.getchildren():
        dot_code += xml_to_dot(child, parent=node_id)
    
    return dot_code


def object_tree_to_dot_string(xml_string):
    root = etree.fromstring(xml_string)
    dot_code = 'digraph Tree {\n'
    dot_code += xml_to_dot(root)
    dot_code += '}'
    return dot_code


def convert_xml_to_graph(xml_string):
    # Convert XML to DOT format
    dot_code = object_tree_to_dot_string(xml_string)
    # Create Graph from DOT code
    graph = graphviz.Source(dot_code)
    # Save the graph as an image
    output_file = "tree_graph"
    graph.format = 'png'    
    graph.render(output_file, view=False)