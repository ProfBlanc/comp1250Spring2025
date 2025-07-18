import csv

with open("gradebook.csv", "r+") as fo:
    reader = csv.reader(fo)
    for row in reader:
        print(row)
        print(row[0], row[1], row[2])
        print("*" * 20)