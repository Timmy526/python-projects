#Initialize Variables
total_cost = 0              #Total Cost
portion_down_payment = 0    #Portion Down Payment
current_savings = 0         #Current Savings
r = 0.04                    #Annual Return Rate
annual_return = 0           #Annual Return Amount
annual_salary = 0           #Annual Salary
portion_saved = 0           #Portion Saved
monthly_salary = 0          #Monthly Salary
months = 0                  #Months Counter
amount_salary = 0           #Amount Salary

#Asking and Retrieving User Input
annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to be saved (in decimal): '))
total_cost = float(input('Enter the cost of your dream home: '))

#Calculate Portion Down Payment
portion_down_payment = 0.25 * total_cost 

#Calculate Annual Return
annual_return = (current_savings * r) / 12

#Calculate Monthly Salary
monthly_salary = annual_salary / 12

#Calculate Portion Saved
amount_saved = portion_saved * monthly_salary

#Calculate how many months needed to put a down payment on the home.
while (current_savings <= portion_down_payment):
    #Incrementing Months to keep track of how many months needed
    months = months + 1 

    #Return Rate conversion
    current_savings = (amount_saved + (current_savings * r / 12)) + current_savings 

#Print out how many months it will take
print('Number of months: %d' %months)
