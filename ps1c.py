#Initialize variables
starting_salary = 0
current_savings = 0.0
steps = 0
annual_salary = 0
monthly_saved = 0
semi_annual_rise = 0.07 
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36
min_integer = 0        
max_integer = 10000    
portion_saved = int((max_integer + min_integer) / 2)
steps = 0
found = False
i = 0

#Prompt user for starting salary
starting_salary = int(input("Enter the starting annual salary: "))

#Calculates how many steps, and best savings rate
while abs(min_integer - max_integer) > 1:
    #Counter for how many steps in the bisection search
    steps = steps + 1 

    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings = (monthly_return + monthly_saved) + current_savings

        if abs(current_savings - portion_down_payment) < 100:
            min_integer = max_integer
            found = True
            break
        elif current_savings > portion_down_payment + 100:
            break
        
        if i % 6 == 0:
            annual_salary = (annual_salary * semi_annual_rise)+annual_salary
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        min_integer = portion_saved
    elif current_savings > portion_down_payment + 100:
        max_integer = portion_saved
    
    portion_saved = int((max_integer + min_integer) / 2)
    
if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years")