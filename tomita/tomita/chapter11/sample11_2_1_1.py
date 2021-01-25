import csv

with open('sample11_2_1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Alice', 23, 'F'])
    writer.writerow(['Bob', 31, 'M'])
    writer.writerow(['Charlie', 26, 'M'])
