import os
import xml.etree.ElementTree as ET

path = 'C:\python_program'
file_find = 'test.xml'

def change_xml(path,file_find):
    for file in os.listdir(path):
        if file.endswith(file_find):
            xmlfile = os.path.join(path, file_find)
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            print(root)
            print(ET.tostring(root, encoding="utf-8").decode('utf-8'))
            for child in root.iter(file_find):
                print(child.attrib)

change_xml(path, file_find)