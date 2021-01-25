import xml.etree.ElementTree as et

total = 0
count = 0

tree = et.parse('sample11_3.xml')
root = tree.getroot()

for i in root:
    age = int(i.find('age').txt)

    total += age
    count +=  1

print('{0:.1f}'.format(total / count  ))