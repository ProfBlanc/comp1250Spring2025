import csv
filename = "test.txt"
with open(filename) as fo:
    reader = csv.reader(fo, delimiter=",",lineterminator="\n")
    for row in reader:
        print(row, row[0], row[1], row[2])