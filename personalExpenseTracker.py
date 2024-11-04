#personalExpenseTracker.py

# Initialize the list to store expense entries
expenses = []

# Initialize the set to store unique categories
categories = set()

# Function to add an expense
def add_expense(name, amount, category):
    count=0
    while True:
        if count<2:
            name=input("enter name of expense : ")
            amount=int(input("enter amount for expense : "))
            category=input("enter enpense category : ")
    # Add the expense as a tuple (name, amount) to the list
            expenses.append((name, amount, category))
    # Add the category to the set (to ensure unique categories)
            categories.add(category)
            count+=1
        else:
            break

# add_expense function calling
add_expense('name', 'amount', 'category')

# Display all expenses
print("Expenses Logged:", expenses)

# Display unique categories
print("Categories:", categories)

# Create a dictionary summary where key is category and value is total amount spent
summary = {category: sum(amount for name, amount, cat in expenses if cat == category) for category in categories}

# Display the summary of expenses by category 
print("Expense Summary by Category:",summary)
