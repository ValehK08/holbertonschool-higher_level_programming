import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.set("type", type(value).__name__)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    s = {}
    for child in root:
        s[child.tag] = child.attrib
    return s