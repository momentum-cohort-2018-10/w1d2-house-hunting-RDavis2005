annual_salary = int(input("Enter your annual salary:"))

monthly = annual_salary / 12

portion_saved = float(input("Enter the percent of your salary to save,as a decimal:"))

annual_rate_of_return = float(input("Enter the expected annual rate of return:"))

total_cost = int(input("Enter the cost of your dream home:"))

percent_to_save = float(input("Enter the percent of your home's cost to save as a down payment:"))

current_savings = 0
month = 0
r = annual_rate_of_return / 12

down_payment = int(total_cost * percent_to_save)

while current_savings <= down_payment:
    month = month + 1
    current_savings += (current_savings * r) + (portion_saved * monthly)
    print(month)
print("It will take you", (month), "months to have enough money for the down payment.")