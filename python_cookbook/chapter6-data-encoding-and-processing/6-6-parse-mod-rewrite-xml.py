from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')
root = doc.getroot()
print(root)

# remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# insert a new element after <nm> ... <nm>
# python 3.9中已经移除
root.getchildren().index(root.find('nm'))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# write back to a file
doc.write('newpred.xml', xml_declaration=True)

