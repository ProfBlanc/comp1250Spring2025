import csv
filename = "test.txt"
header_columns = "Name,Age,Grade".split(",")
with open(filename) as fo:
    reader = csv.DictReader(fo, delimiter=",",
                            lineterminator="\n", fieldnames=header_columns)

    for row in reader:
        print(row["Name"], row["Age"], row["Grade"])
