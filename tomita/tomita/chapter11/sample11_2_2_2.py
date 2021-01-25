import csv
with open('sample11_2_2.csv', 'r', newline='') as f:
    cin = csv.DictReader(f)
    for row in cin:
        print(row)