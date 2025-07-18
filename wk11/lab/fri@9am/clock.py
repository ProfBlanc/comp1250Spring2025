def show_time():
    print('show time called')

def countdown(starting_value):
    print('countdown called')

def timer(ending_value):
    print('timer called')

def set_alarm(alarm_time):
    print('setting alarm called')

options = "show_time,countdown,timer,set_alarm".split(",")

def main():
    print("Welcome to our app")
    option = input("Choose from one of the following options\n\n" + "\n".join(options) + "\n\n")
    match option:
        case "show_time":
            show_time()
        case "countdown":
            starting_value = int(input("Enter starting time: "))
            countdown(starting_value)
        case "timer":
            ending_value = int(input("Enter ending time: "))
            timer(ending_value)
        case "set_alarm":
            alarm_time = input("Enter alarm time")
            set_alarm(alarm_time)

if __name__ == '__main__':
    main()