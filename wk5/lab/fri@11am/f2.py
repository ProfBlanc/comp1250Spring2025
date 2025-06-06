courses = dict()
courses['Monday'] = list()
courses['Monday'].append({'11am': "comp1250 lecture"})
courses['Monday'].append({'9am': "comp3105 lecture"})
courses['Friday'] = list()

courses['Friday'].append({'9am': "comp1176 lab"})
courses['Friday'].append({'11am': "comp1250 lab"})

print(courses)

# allow the user to guess either the day of the week or time of the day and output the courses that correspond
user_input = input("Enter either a dow or a time: ").lower()
if user_input.endswith("day") or user_input.isalpha():
    key = user_input.title()
    if key in courses:
        print("The courses you have on", key, "are", courses[key])
    else:
        print("You have no courses on", key)
elif user_input.endswith("am") or user_input.endswith("pm"):
    target_time = user_input
    courses_that_match_time = list()
    for key in courses:
        for item in courses[key]:
            for cur_time in item:
                if cur_time == target_time:
                    courses_that_match_time.append(item[cur_time])
    print("Here are the courses that you have at", target_time, ": ", courses_that_match_time)
else:
    print("Invalid input")
 
    
