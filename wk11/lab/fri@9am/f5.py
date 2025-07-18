import csv
filename = "test1.csv"
header_columns = "Name,Age,Grade".split(",")

data = [
    {"Name": "John", "Age": "20", "Grade": "100"},
    {"Name": "Mary", "Age": "21", "Grade": "99"},
    {"Name": "Sally", "Age": "22", "Grade": "98"}
]


with open(filename, "w") as fo:
    writer = csv.DictWriter(fo, delimiter=",",
                            lineterminator="\n", fieldnames=header_columns)

    writer.writeheader()
    writer.writerows(data)