import xml.etree.ElementTree as et

tree = et.parse('sample11_3.xml')
root = tree.getroot()
print('ルート要素のタグ名:{}'.format(root.tag))
print('ルート直下の要素数:{}'.format(len(root)))

for person in root:
    name = person.find('name').text
    age = person.find('age').text
    gender = person.find('gender').text
    print('名前:{},年齢:{},性別:{}'.format(name, age, gender))