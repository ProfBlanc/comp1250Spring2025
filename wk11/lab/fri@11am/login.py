import csv
filename = "logins.csv"

username = input("Enter your username: ")
password = input("Enter your password: ")


with open(filename, "r") as fo:
    reader = csv.DictReader(fo, fieldnames=["username", "password"])

    found = False

    for row in reader:
        if row["username"] == username and row["password"] == password:
            found = True
            break

    print("You have successfully logged in" if found else "Invalid Login")