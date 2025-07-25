class Mortgage:
    def __init__(self, borrowing_value, interest_rate, monthly_payments):
        self.borrowing_value = borrowing_value
        self.interest_rate = interest_rate if interest_rate >0 and interest_rate <1 else round(interest_rate /100, 2)
        self.interested_payed = 0
        self.balance_remaining = self.borrowing_value
        self.monthly_payments = monthly_payments
    def __str__(self):
        return (f"You are borrowing {self.borrowing_value} "
                f"at a interest_rate of {self.interest_rate}%")
    def chart_payments(self):
        months = 0
        years = 1
        while self.balance_remaining > 0:
            months += 1
            if months % 12 == 0:
                months = 1
                years += 1

            interest_for_this_month = round(self.balance_remaining * self.interest_rate / 12, 2)
            principal_value_payed = round(self.monthly_payments - interest_for_this_month, 2)

            self.interested_payed += interest_for_this_month
            self.balance_remaining -= principal_value_payed
            print(f"In month {months} of year {years}, you have accrued {interest_for_this_month} "
                  f"in interest. You paid {self.monthly_payments}. "
                  f"{principal_value_payed} was deducted from your "
                  f"balance of {round(self.balance_remaining, )}. ")
        print(f"Overall, you paid {self.interested_payed + self.borrowing_value} "
              f"for a loan of {self.borrowing_value}. That's a difference of {self.interested_payed}")

m1 = Mortgage(1000, 3, 5.15)
print(m1)
m1.chart_payments()

# m2 = Mortgage(1000, 0.04, 10)
# print(m2)