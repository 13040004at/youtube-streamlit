import csv

total = 0
count = 0
with open('sample11_2_1.csv', 'r' ) as f:
    reader = csv.reader(f)
    for i in reader:
           age = int(i[1])
           total += age
           count += 1


print('{0:.1f}'.format(total / count  ))


