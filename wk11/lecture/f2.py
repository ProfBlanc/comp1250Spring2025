from example2_data import *

with open("gradebook.csv", "w") as fo:
    for header_column in header:
        fo.write(header_column + ",")
    fo.write("\n")

    for row in data:
        for column in row:
            fo.write(column + ",")
        fo.write("\n")