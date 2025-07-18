import csv
import os
import sys

username = input("Enter your username: ")
password = input("Enter your password: ")

filename = "logins.csv"
fields = "username,password".split(",")

with open(filename, "a+") as fo:
    reader = csv.DictReader(fo, fieldnames=fields, lineterminator='\n')
    writer = csv.DictWriter(fo, fieldnames=fields, lineterminator='\n')

    # determine if username is already in use
    is_in_use = False
    fo.seek(0)  # make pointer start at end of file
    for row in reader:
        if username == row[fields[0]]:
            is_in_use = True
            break

    if is_in_use:
        print("Username is already in use", file=sys.stderr)
    else:
        fo.seek(0, os.SEEK_END)
        file_size_length_in_bytes = fo.tell()
        print("The file size is", file_size_length_in_bytes)
        if file_size_length_in_bytes == 0:
            writer.writeheader()

        data = {fields[0]: username, fields[1]: password}
        writer.writerow(data)



