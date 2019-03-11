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
            #print(root)
            #print(ET.tostring(root, encoding="utf-8").decode('utf-8'))
            for child in root.iter('movie'):
                print(child.attrib)
            b2tf = root.find("./genre/decade/movie[@title]")
            print(type(b2tf))
            b2tf.attrib["title"] = "Back To The Future Aalam Geer Rana"
            print(b2tf.attrib)
            tree.write(xmlfile)
            tree =ET.parse(xmlfile)

change_xml(path, file_find)