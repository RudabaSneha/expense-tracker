from tracker import Expense 
import calendar
import datetime
def main():
    budget = float(input('what is your monthly budget? '))
    print(f"Expense tracker")
    expense_file_path = "expenses.csv"
    
    # get user input for costs
    expense = get_expense()
    
    #put expense in a file
    transfer_data(expense, expense_file_path)
    #read file and summarize expenses
    summarize_expenses(expense_file_path, budget)
    
def get_expense():
    purchase = input('Enter item: ')
    amount = float(input('Enter item price: '))
  
  
    categories = [
        'food/drink', 'entertainment', 'personal', 'car', 'bills', 'insurance', 'home', 'other'
        ]
    
    while True:
        print('Select a category')
        numbered_categories = enumerate(categories)
        for i, value in numbered_categories:
            print(f' {i+1}.) {value}')
        
        value_range = f'1-{len(categories)}'
        try:
            user_range_number = int(input(f"Enter the number which best matches your category {value_range}: "))-1
                
        except Exception:
            print("Invalid category. Try again! ")
        
        if user_range_number in range(len(categories)):
            selected_category = categories[user_range_number]
            new_user_expense = Expense(name = purchase, type= selected_category, price = amount)
            return new_user_expense
        
        break
    
    

def transfer_data(expense: Expense, expense_file_path):
    print(f"transferring expense {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name}, {expense.type},{expense.price}\n")

def summarize_expenses(expense_file_path, budget):
    print("summarizing your expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            purchase,categories,amount = line.strip().split(",")
            line_expense = Expense(name=purchase,type=categories, price=float(amount))
            
            
            expenses.append(line_expense)
    
    amount_by_category = {}
    
    for expense in expenses:
        key = expense.type
        if key in amount_by_category:
            amount_by_category[key] += expense.price
        else:
            amount_by_category[key] = expense.price
    
    
    
    for key, price in amount_by_category.items():
        print(f"  {key}:  ${price:.2f}")
        
    total_spent = sum([i.price for i in expenses])
    print(blue(f'Money spent this month: ${total_spent:.2f} '))

    remaining_budget = budget - total_spent
    print(f'Budget Remaining: ${remaining_budget:.2f}')
    
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day 
    
    daily_budget = remaining_budget/ remaining_days
    print(blue(f"Budget per day is ${daily_budget:.2f}"))
    
    #coloring terminal text
def blue (text):
    return f"\033[96m{text}\033[0m"


if __name__ == '__main__':
    main()