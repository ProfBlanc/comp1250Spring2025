import re
import sys
import os

root_path = "data"  # main working directory


def setup():
    if not os.path.exists(root_path):
        os.mkdir(root_path)


def prompt_question(question):
    return input(question + ": ")


def validate_date(data):
    """
    This function validates a date in the format of YYYY-mm-dd
    (year, month, day)
    After passing the date through a regex, we will determine if month and day combo match
    :param data: string containing date with expected format above
    :return: tuple of Year, Month, Day or None

    >>> validate_date("2025-07-14")
    (2025, 7, 14)
    >>> validate_date("2025/07/14")
    (2025, 7, 14)
    >>> validate_date("2020/17/144")
    None
    """
    regex = r"\d{4}[/-]\d{2}[/-]\d{2}"
    if re.match(pattern=regex, string=data):
        separator = "-" if "-" in data else "/"
        components = data.split(separator)
        year = int(components[0])
        month = int(components[1])
        day = int(components[2])
        if year >= 2000 and year <= 2050 and month >= 1 and month <= 12 and day >= 1 and day <= 31:
            # TODO: create conditions to test invalid month-day combinations
            return year, month, day
        else:
            return None
    else:
        return None


def validate_time(data):
    regex = r"\d{1,2}\s?(am|pm|h)?"
    return True if re.match(pattern=regex, string=data, flags=re.I) else False

def validate_details(data):
    return len(data.strip()) > 1  # details must be at least 1 character

def add_event_to_calendar(event_date, date, event_time, event_details):
    print(f"You want to add the event on {event_date}, at {event_time}, with details of {event_details}")
    # date = (YEAR, MONTH, DAY)

    year_folder = os.path.join(root_path, f"{date[0]}")

    month_folder = os.path.join(year_folder, f"{date[1]}")

    day_file = os.path.join(month_folder, f"{date[2]}.txt")

    # determine if folder with year exists. if not, add folder
    if not os.path.exists(year_folder):
        os.mkdir(year_folder)

    if not os.path.exists(month_folder):
        os.mkdir(month_folder)

    content = f"{event_time}: {event_details}\n"

    # version 1
    # fo = open(day_file, "a")
    # fo.write(content)
    # fo.close()

    # version 2
    # print(content, end='', file=open(day_file, "a"))

    # version 3
    with open(day_file, "a") as fo:
        fo.write(content)

def add_event():
    event_date = prompt_question("Enter the date of the event")
    date = validate_date(event_date)

    event_time = prompt_question("Enter the time of the event")
    res1 = validate_time(event_time)

    event_details = prompt_question("Enter the details of the event")
    res2 = validate_details(event_details)

    if date is not None and res1 and res2:
        add_event_to_calendar(event_date, date, event_time, event_details)
    else:
        print("Sorry, but you entered incorrect data", file=sys.stderr)


def main():
    setup()
    print("Welcome to our Calendar Module")
    add_event()


if __name__ == '__main__':
    main()
