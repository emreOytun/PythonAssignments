# Initialize the variables.
contribution = 0
startAge = 0
retirementAge = 0

# Read the inputs and make the controls.
deposit = int(input("Enter the amount of deposit: "))
if (deposit <= 0) :
    print("Invalid deposit value!")

if (deposit > 0) :
    contribution = int(input("Enter monthly contribution: "))
    if (contribution <= 0) :
        print("Invalid contribution value!")

if (deposit > 0 and contribution > 0) :
    startAge = int(input("Enter your age: "))
    if (startAge <= 0) :
        print("Invalid age value!")

if (deposit > 0 and contribution > 0 and startAge > 0) :
    retirementAge = int(input("Enter your retirement age: "))
    if (retirementAge <= 0) :
        print("Invalid retirement age value!")

# Check start age and retirement age to be consistent.
if (startAge > retirementAge) :
    print("Invalid retirement age value!")

elif (deposit > 0 and contribution > 0 and startAge > 0 and retirementAge > 0) :
    # Find the fund for each ages.
    fund = deposit
    for year in range(retirementAge - startAge) :
        for month in range(1, 13) :
            if (year < 10) :
                fund += (fund * 0.002)
            else :
                fund += (fund * 0.003)
            
            if (month == 2 or month == 5 or month == 8 or month == 11) :
                fund += contribution    

        print("At the end of year " + str(year + 1) + " the fund balance is " + str(fund))

    retirementPayment = int(input("Enter the monthly retirement payment you want to receive: "))
    if (retirementPayment <= 0) :
        print("Invalid monthly retirement payment!")
    else :
        # Find the fund after 10 years.
        for year in range(10) :
            for month in range(1, 13):
                fund -= retirementPayment
                fund += fund * 0.003

        if (fund <= 0) :
            print("There is not enough money in the fund for this amount of monthly payment.")
        else :
            print("At the end of 10 years, you will receive the remaining balance of " + str(fund))
        

