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
semi_annual_raise = 0       #Semi Annual Raise Amount
amount_saved = 0            #Amount Saved

#Asking and Retrieving User Input
annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to be saved (in decimal): '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter your semi annual raise amount (in decimal): '))

#Calculate Portion Down Payment
portion_down_payment = 0.25 * total_cost 

#Calculate Annual Return
annual_return = (current_savings * r) / 12

#Calculate Monthly Salary
monthly_salary = annual_salary / 12

#Calculate Portion Saved
amount_saved = monthly_salary * portion_saved

#Calculate how many months needed to put a down payment on the home.
while (current_savings <= portion_down_payment):

    #Incrementing Months to keep track of how many months needed
    months = months + 1 

    #Return Rate conversion
    current_savings = ((amount_saved + (current_savings * (r / 12))) + current_savings)

    #If the amount of months is divisible by 6
    if months % 6 == 0: 
        
        #Take the new annual salary with the addition of the semiannual raise
        annual_salary = ((1 + semi_annual_raise) * annual_salary) 
        
        #Take the new monthly salary
        monthly_salary = annual_salary / 12
        
        #Take the new amount saved
        amount_saved = monthly_salary * portion_saved
    
#Print out how many months it will take
print('Number of months: %d' %months)
