import json

total = 0
count = 0

with open('sample11_4_1.json', 'r') as f:
        people = json.load(f)
        for i in people:
            total += i['age']
            count += 1

print('{0:.1f}'.format(total / count  ))