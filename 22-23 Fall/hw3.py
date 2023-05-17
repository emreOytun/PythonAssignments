
# Read and check the desired number of vacation days.
isRead = True
numOfvacationDays = int(input("Desired number of vacation days : "))
if (numOfvacationDays < 4) :
    isRead = False
    print("Error! Desired vacation days cannot be less than 4.")

# Read and check the off days.
if (isRead) :
    offDay1 = int(input("Off-day1 (1-7) : "))
    offDay2 = int(input("Off-day2 (1-7) : "))
    if (offDay1 == offDay2) :
        isRead = False
        print("Off-days must be different.")
    
    elif (not (1<=offDay1 and offDay1<=7 and 1<=offDay2 and offDay2<=7) ) :
        isRead = False
        print("Day numbers should be in range 1-7.")

# 1) Read number of weeks.
# 2) Calculate total money.
if (isRead) :
    numOfWeeks = int(input("Number of weeks : "))

    # Calculate the total money.
    totalMoney = 0
    for weekNum in range(1, numOfWeeks+1) :
        for dayNum in range(1, 8) :
            if (dayNum != offDay1 and dayNum != offDay2) :
                totalMoney += weekNum*dayNum

    print(totalMoney)

    for vacationDay in range(1, numOfvacationDays+1) :
        if (totalMoney <= 0) :
            print("You do not have enough money for day " + str(vacationDay))
        
        else : 
            dayOfWeek = vacationDay%7
            spendingMoney = 0

            # If the mod of vacation day according to 7 is 6 or 0, it means it's weekend.
            if (dayOfWeek == 6 or dayOfWeek == 0) :
                spendingMoney = 2*(10+vacationDay)
            else :
                spendingMoney = 10+vacationDay

            totalMoney -= spendingMoney
            if (totalMoney > 0) :
                print("At the end of day " + str(vacationDay) + " you have $ " + str(totalMoney) + " left")
            
            else :
                print("You do not have enough money for day " + str(vacationDay))
