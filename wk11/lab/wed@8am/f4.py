import csv

from wk11.lecture.example2_data import *


values = list()

row1 = dict.fromkeys(header)
row1[header[0]] = "Ben"
row1[header[1]] = 20
row1[header[2]] = 100

row2 = dict.fromkeys(header)
row2[header[0]] = "Mary"
row2[header[1]] = 21
row2[header[2]] = 99

row3 = dict.fromkeys(header)
row3[header[0]] = "John"
row3[header[1]] = 22
row3[header[2]] = 98

values.append(row1)
values.append(row2)
values.append(row3)

print(values)

with open("gradebook3.csv", "w") as fo:
    dict_writer = csv.DictWriter(fo, fieldnames=header, lineterminator="\n")

    dict_writer.writeheader()
    dict_writer.writerow(row1)
    dict_writer.writerows(values)

