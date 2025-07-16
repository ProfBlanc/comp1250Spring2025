from example2_data import *
import csv


with open("gradebook1.csv", "w") as fo:
    writer = csv.writer(fo, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(data)
