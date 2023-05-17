def format_data(name, designation, willingness):
    resultName = ""
    names = name.lower().split()
    subCount = 0
    for subName in names :
        if (len(subName) == 2) :
            resultName += subName
        else :
            resultName += subName.capitalize()
        if (subCount < len(names)-1) :
            resultName += " "

    resultDesignation = ""
    if (designation.startswith("d") or designation.startswith("D")) :
        resultDesignation = "Dean"
    elif (designation.startswith("p") or designation.startswith("P")) :
        resultDesignation = "Professor"
    elif (designation.endswith("d") or designation.endswith("D")) :
        resultDesignation = "Student"
    elif (designation.endswith("f") or designation.endswith("F")) :
        resultDesignation = "Staff"

    resultWillingness = ""
    if (willingness.startswith("y") or willingness.startswith("Y")) :
        resultWillingness = "Yes"
    else :
        resultWillingness = "No"
    return resultName, resultDesignation, resultWillingness

def calculate_price(position, date, willingness):
    amount = 0
    if (willingness.startswith("y") or willingness.startswith("Y")) :
        year = date[6:10]
        year = int(year)
        if (position == "Professor") :
            if (year < 2010) :
                amount = 400
            elif (2010 <= year and year <= 2020) :
                amount = 350
            else :
                amount = 300
                
        elif (position == "Dean") :
            if (year < 2010) :
                amount = 450
            elif (2010 <= year and year <= 2020) :
                amount = 400
            else :
                amount = 350

        elif (position == "Student") :
            amount = 200
        else :
            amount = 250

    return amount

wantsContinue = True
wantsCalculation = input("Do you want to check payable amount for the trip: ")
if (not wantsCalculation.startswith("y") and not wantsCalculation.startswith("Y")) :
    wantsContinue = False

while (wantsContinue) :
    name = ""
    position = ""
    date = ""
    wilingness = ""

    validInput = False
    name = input("Enter your full name: ")
    if (name.__contains__(" ")) :
        validInput = True
    while (not validInput) :
        name = input("Enter your full name with space(s): ")
        if (name.__contains__(" ")) :
            validInput = True
    
    position = input("Enter your position: ")

    validInput = False
    date = input("Enter your start date as DD.MM.YYYY: ")
    while (not validInput) :
        if (len(date) == 10) :
            day = date[0:2]
            month = date[3:5]
            year = date[6:10]
            if (day.isdigit() and month.isdigit() and year.isdigit()) :
                day = int(day)
                month = int(month)
                year = int(year)

                if (1 <= day and day <= 31) and (1 <= month and month <= 12) and (1993 <= year and year <= 2023):
                    validInput = True

        if (not validInput) :
            date = input("Invalid. Enter the start date in correct format: ")

    wilingness = input("Would you like to partipicate in event: ")
    name, position, wilingness = format_data(name, position, wilingness)

    amount = calculate_price(position, date, wilingness)
    print()
    print("The Details of individual are:")
    print("Name = ", name)
    print("Position = ", position)
    print("Start Year = ", year)
    print("Willingness = ", wilingness)
    print("The individual's expenditure will be ", amount, " USD.")
    print()

    wantsCalculation = input("Do you want to check for someone else: ")
    if (wantsCalculation.startswith("y") or wantsCalculation.startswith("Y")) :
        wantsContinue = True
    else :
        wantsContinue = False

print("Have a good day!")

