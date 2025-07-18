import csv

col_names = "Name,Age,Grade".split(",")

with open("gradebook.csv", "r+") as fo:
    dict_reader = csv.DictReader(fo, fieldnames=col_names,
                                 lineterminator="\n")

    for row in dict_reader:
        print(row)
        print(row[col_names[0]], row['Age'], row['Grade'])
        print("*" * 20)
