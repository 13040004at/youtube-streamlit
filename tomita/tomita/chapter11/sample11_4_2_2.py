import json

people = [
    {'name': 'David', 'age': 17,'gender': 'M'},
    {'name': 'Ellie', 'age': 28,'gender': 'F'},

]

with open('sample11_4_2.json', 'w')as f:
    json.dump(people,f,indent=2)