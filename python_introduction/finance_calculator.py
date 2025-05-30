# Ask the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a yearly interest rate of 5%
interest_rate = 0.05

# Calculate projected savings after one year, including interest
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Show the results 
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" +
str(round(annual_savings, 2)))
