# print(), input(), round(), int(), str(), float(), bool()

print(  min(1, -1, 10)  )  # -1
print(   max(1, -1, 10)  )  # 10
print(    max(     len("ben"), len("benny"), len("benjamin")   )  )  # 

# len(), min(), max()

# ask the user for their hourly rate
# ask the user how many hours they work per week
# calcualate a monthly budget
# output the montly gross budget
# calculate the gross budget

# apply the 50-30-20 rule: 
# output that 50% of your money should be used for needs
# output that 30% for your wants
# output that 20% for your savings

print("Welcome to our financial planning app")
print("You will enter your hourly rate and", end=" ")
print("how many hours you work per week, and we will", end=" ")
print("output the numbers to stick with the 50-30-20 rule")

hourly_rate = input("What is your hourly rate? ")
hourly_rate = round( float(hourly_rate), 2)


hours_worked = round( float(input("How many hours do you work per week? ")), 2)

gross_monthly_income = round(hourly_rate * hours_worked * 4, 2)

net_month_income = round(gross_monthly_income * 0.85, )

needs = round(net_month_income / 2, 2)
wants = round(net_month_income * .3, 2)
savings = round(net_month_income - (needs + wants), 2)

print(f"Your hourly rate is ${hourly_rate}/hour.")
print("Your hourly rate is $",hourly_rate, "/hour.", sep="")
print("Your hourly rate is $" + str(hourly_rate) + "/hour.")

print(f"You work {hours_worked} per week")
print(f"You make ${gross_monthly_income} per month (gross), and ${net_month_income} per month net")
print(f"Following the 50-30-20 rule, you should spend ${needs} on your needs, ${wants} on your wants, and ${savings} should go into savings")
