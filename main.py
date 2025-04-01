print('Hello, World!')
import xml.etree.ElementTree as ET
from lxml import etree


parser = etree.XMLParser(recover=True,encoding='utf-8')
xml_file = ET.parse('example2.xml',parser=parser)
import re
root = xml_file.getroot()


# title = root.find('.//ce:title', namespaces={'ce': 'http://www.elsevier.com/'})
# print( title)

# print(root)
# parser = ET.XMLParser(encoding='utf-8')
# xml_file = ET.parse('example2.xml',parser=parser)
# tree = ET.XMLParser('example.xml')
# tree = ET.parse('example.xml')
# root = tree.getroot()



# print(root.tag)
# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# print(root[0][1].tag, root[0][1].attrib, root[0][1].text)

# head_element = root.find('head')

# ce_element = head_element.findall('ce')

# print("ce_element", ce_element)

# for child in head_element:
#     print(child.tag, child.attrib)

# print("head_element", head_element.tag, head_element.attrib)

# print("root", root)

# title = root.find('head')
# print("Title:", title.text)

namespace = {'ce': 'http://www.elsevier.com/', 'xlink': 'http://www.w3.org/'
}

# Iterate and print all ce:label elements
# for label in root.findall('.//ce:label', namespaces=namespace):
#     print(label.text)

# for label in root.iterfind('.//ce:figure', namespaces=namespace):
#     print(label.tag, label.attrib)

print(root.findall("."))

print(root.findall("./"))

# print(root.findall(".//"))

print(root.find('.//ce:surname', namespaces=namespace))

item_info= root.find('./item-info')

# for child in item_info:
#     print(child.tag)

figures = root.xpath('//ce:figure', namespaces=namespace)
print("1. All ce:figure elements:")
for figure in figures:
    print(figure.tag, figure.attrib)

first_label = root.xpath('//ce:label[1]', namespaces=namespace)
print("\n2. First ce:label element:")
if first_label:
    print(first_label[0].text)


figure_labels = root.xpath('//ce:figure/ce:label', namespaces=namespace)
print("\n3. ce:label elements within ce:figure elements:")
for label in figure_labels:
    print(label.text)


figure = root.xpath('//ce:figure[@id="f0010"]', namespaces= namespace)
print("\n4. ce:figure element with id='f0010':")
if(figure):
    # print(figure[0].tag, figure[0].attrib, figure[0].text)
    print(figure[0].tag, figure[0].attrib, figure[0].text)
    print(figure)

# simple_paras_text = root.xpath('//ce:simple-para/text()', namespaces=namespace)
# print("\n5. Text of all ce:simple-para elements:")
# for text in simple_paras_text:
#     print(text.strip()) 

# simple_paras_text1 = root.xpath('//ce:simple-para', namespaces=namespace)
# print("\n5. Text of all ce:simple-para elements:")
# for text in simple_paras_text1:
#     print(text.text) 

# parent_of_first_label = root.xpath('//ce:label[1]/parent::*', namespaces=namespace)
# print("\n6. Parent of the first ce:label element:")
# if parent_of_first_label:
#     print(parent_of_first_label[0].tag)

# figure_attributes = root.xpath('//ce:figure/@*', namespaces=namespace)
# print("\n7. All attributes of ce:figure elements:")
# for attribute in figure_attributes:
#     print(attribute)


# figure_attributes = root.xpath('//ce:figure/@*', namespaces=namespace)
# print("\n7. All attributes of ce:figure elements1:")
# for attribute in figure_attributes:
#     print(attribute)
specific_link = root.xpath('//ce:link[@xlink:href="pii:S0169433224021974/gr1"]', namespaces=namespace)
print("\nce:link element with specific href:")
if specific_link:
    print(specific_link[0].tag, specific_link[0].attrib)

# captions = root.xpath('//ce:caption', namespaces=namespace)
# print("\n9. ce:caption elements:")
# for caption in captions:
#     print(caption.tag, caption.attrib)

# inf_elements = root.xpath('//ce:inf', namespaces=namespace)
# print("\n10. ce:inf elements:")
# for inf in inf_elements:
#   print(inf.tag, inf.text)


labels = root.xpath('//ce:label', namespaces=namespace)
for label in labels:
    label.text = "Fig. 1"


figures = root.xpath('//ce:figure', namespaces=namespace)
if figures:
    figures[0].set("modified", "true") 


link_to_remove = root.xpath('//ce:link[@xlink:href="pii:S0169433224021974/gr2"]', namespaces=namespace)
if link_to_remove:
    link_to_remove[0].getparent().remove(link_to_remove[0]) 

captions = root.xpath('//ce:caption', namespaces=namespace)
if captions:
    new_para = etree.Element("{http://www.elsevier.com/}simple-para") 
    new_para.text = "This is a new paragraph."
    captions[0].append(new_para) 

if figures:
  figures[0].set("id", "modified_id")

if len(figures) > 1:
  for attr in list(figures[1].attrib.keys()):
    del figures[1].attrib[attr]

new_figure = etree.Element("{http://www.elsevier.com/}figure")
new_figure.set("id", "f0015")
root.find(".//ce:floats",namespaces=namespace).append(new_figure)

new_label = etree.Element("{http://www.elsevier.com/}label")
new_label.text = "Fig. 1"
new_figure.append(new_label)

output_file = "modified_figures.xml"
tree = etree.ElementTree(root)
tree.write(output_file, encoding="utf-8", xml_declaration=True, pretty_print=True)

print(f"Modified XML written to {output_file}")

