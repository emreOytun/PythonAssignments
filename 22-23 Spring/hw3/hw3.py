# Interest constants
FIRST_TEN_YEARS_INTEREST = 0.002
AFTER_TEN_YEARS_INTEREST = 0.003
MONTHLY_RETIREMENT_INTEREST = 0.003

# Before getting an input, check if there is an invalid input entered before.
# If it is, then go to the end of the program.
# Continue, otherwise.
isRead = True
contribution = -1
start_age = -1
retirement_age = -1
deposit = int(input("Enter the amount of deposit: "))
if (deposit <= 0) :
    print("Invalid deposit value!")
    isRead = False

if (isRead) :
    contribution = int(input("Enter monthly contribution: "))
    if (contribution <= 0) :
        print("Invalid contribution value!")
        isRead = False

if (isRead) :
    start_age = int(input("Enter your age: "))
    if (start_age <= 0) :
        print("Invalid age value!")
        isRead = False

if (isRead) :
    retirement_age = int(input("Enter your retirement age: "))
    if (retirement_age <= 0) :
        print("Invalid retirement age value!")
        isRead = False

if (retirement_age < start_age) :
    print("Invalid retirement age value!")
    isRead = False

# If all inputs are taken successfully, then start to calculate the fund in each year.
if (isRead) :
    totalMoney = deposit
    for yearNum in range(1, retirement_age - start_age + 1) :
        for monthNum in range(1, 13) :
            if (yearNum <= 10) :
                totalMoney += totalMoney * FIRST_TEN_YEARS_INTEREST
            else :
                totalMoney += totalMoney * AFTER_TEN_YEARS_INTEREST

            if (monthNum == 2 or monthNum == 5 or monthNum == 8 or monthNum == 11) :
                totalMoney += contribution    

        print("At the end of year " + str(yearNum) + " the fund balance is " + str(totalMoney))

    # Get the monthly retirement payment from the user.
    # If it is invalid, then go to the end of the program.
    # Continue and calculate the remaining retirement fund after 10 years.
    monthly_retirement_payment = int(input("Enter the monthly retirement payment you want to receive: "))
    if (monthly_retirement_payment <= 0) :
        print("Invalid monthly retirement payment!")
    else :
        for year in range(1, 11) :
            for month in range(1, 13) :
                totalMoney -= monthly_retirement_payment
                totalMoney += totalMoney * MONTHLY_RETIREMENT_INTEREST
        
        if (totalMoney <= 0) :
            print("There is not enough money in the fund for this amount of monthly payment.")
        else :
            print("At the end of 10 years, you will receive the remaining balance of " + str(totalMoney))