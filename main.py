
import xml.etree.ElementTree as ET

# Parse the XML data
with open('eldar.cat', 'r', encoding='utf-8') as file:
    xml_data = file.read()
    
root = ET.fromstring(xml_data)

# Extract text from all elements in the XML

text = ""
# Loop through the children of the element and get their text
with open('output.txt', 'w', encoding='utf-8') as file:
    print("working")
    for child in root.iter():
        
        if child.text == None:
            text = (f'{child.attrib}')
        if child.text != None and child.attrib != None:
            text = (f'{child.attrib} {child.text}')
        file.write(text)
        file.write('\n')
    print("done working")
