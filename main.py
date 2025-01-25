import xml.etree.ElementTree as ET

# Parse the XML data
with open('eldar.cat', 'r', encoding='utf-8') as file:
    xml_data = file.read()
    
root = ET.fromstring(xml_data)

# Extract text from all elements in the XML
unit_list = []
text = ""
# Loop through the children of the element and get their text
with open('output.txt', 'w', encoding='utf-8') as file:
    print("working")
    for child in root.iter():
        # Remove 'typeId' from attributes
        if 'typeId' in child.attrib:
            del child.attrib['typeId']
        
        if 'id' in child.attrib:
            del child.attrib['id']

        if 'targetId' in child.attrib:
            del child.attrib['targetId']

        # Check if the element has type 'unit'
        if child.attrib.get('type') == 'unit':
            print("this is a unit")
            unit_list.append(child.attrib)
        
        if child.text is None:
            text = (f'{child.attrib}')
        elif child.attrib:
            text = (f'{child.attrib} {child.text}')
        else:
            text = child.text
        file.write(text)
        file.write('\n')
    print("done working")

    for unit in unit_list:
        print(unit)
