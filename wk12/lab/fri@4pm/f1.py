class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return f'Expense {self.name} costs {self.amount}'

class Budget:
    def __init__(self, name, monthly_limit):
        self.name = name
        self.monthly_limit = monthly_limit
        self.current_monthly_costs = 0
        self.expenses = list()
    def add_expense(self, expense):
        if isinstance(expense, Expense) \
                and self.current_monthly_costs + expense.amount <= self.monthly_limit:

            self.expenses.append(expense)
            self.current_monthly_costs += expense.amount

    def __str__(self):
        content = f'Budget {self.name} has the following expenses\n'

        for expense in self.expenses:
            content += f'{expense.name}: {expense.amount}\n'

        return content


expense1 = Expense('Food', 10)
expense2 = Expense('Drink', 5)
expense3 = Expense('Presto', 15)

budget = Budget('Monthly Expenses', 50)
budget.add_expense(expense1)
budget.add_expense(expense2)
budget.add_expense(expense3)
print(budget)