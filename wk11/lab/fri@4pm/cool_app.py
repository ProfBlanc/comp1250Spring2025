"""
allows user to send messages to either a number
or a contact
"""
import csv
import os
import sys

file_users = "users.csv"
header_users = "id,username".split(",")

file_contacts = "contacts.csv"
header_contacts = "owner,friend_user_id".split(",")

file_messages = "messages.csv"
header_messages = "sender_id,recipient_id,message".split(",")


def init_file(file, header):
    if not os.path.exists(file):
        with open(file, "w") as fo:
            writer = csv.DictWriter(fo, fieldnames=header, lineterminator="\n")
            writer.writeheader()


def setup():

    init_file(file_users, header_users)
    init_file(file_contacts, header_contacts)
    init_file(file_messages, header_messages)
def get_user_id(username):
    with open(file_users, "r") as fo:
        reader = csv.DictReader(fo, lineterminator="\n", fieldnames=header_users)
        for row in reader:
            if row[header_users[1]] == username:
                return row[header_users[0]]
    return None


def create_user(username):
    with open(file_users, "a+") as fo:
        writer = csv.DictWriter(fo, lineterminator="\n", fieldnames=header_users)

        fo.seek(0, os.SEEK_END)  # putting cursor at end of file
        fo.seek(0)  # putting cursor at start of file

        lines = fo.readlines()  # all lines as list
        last_line = lines[-1] # 100,benny
        last_id = last_line.split(",")[0]
        last_id_num = int(last_id) if last_id.isnumeric() else 0
        last_id_num += 1

        writer.writerow({header_users[0]: str(last_id_num),
                         header_users[1]: username})




setup()
me = input("Enter your username: ")

my_id = get_user_id(me)

if my_id is None:
    # print("User not found!", file=sys.stderr)
    print("user not found.")
    answer = input("Would you like to create this user? y/n")
    if answer.lower() == "y":
        my_id = create_user(me)


options = "1)View Contacts\n2)View Messages\n3)Add Contact\n4)Create Message"

choice = int(input("What would you like to do?\n"+ options + "\n:"))

"""
users
    id, username
contacts
    owner, friend_user_id
messages
    sender_id, recipient_id, message_text
"""