def calculate_price(position, date, willingness):
    calculated_price = 0
    if willingness.startswith("Y") or willingness.startswith("y") :
        year = date[6:10]
        year = int(year)

        if position == "Student" :
            calculated_price = 200
        elif position == "Staff" :
            calculated_price = 250
        elif position == "Professor" :
            if (year < 2010) :
                calculated_price = 400
            elif 2010 <= year and year <= 2020 :
                calculated_price = 350
            else :
                calculated_price = 300    
        else :
            if year < 2010 :
                calculated_price = 450
            elif 2010 <= year and year <= 2020 :
                calculated_price = 400
            else :
                calculated_price = 350

    return calculated_price

def format_data(name, designation, willingness):
    if willingness.startswith("Y") or willingness.startswith("y") :
        willingness = "Yes"
    else :
        willingness = "No"
    
    formatted_name = ""
    names = name.split()
    count = 0
    for subName in names :
        subName = subName.lower()
        if not len(subName) == 2 :
            formatted_name += subName.capitalize()
        else :
            formatted_name += subName
        if count < len(names)-1 :
            formatted_name += " "

    if designation.startswith("P") or designation.startswith("p") :
        designation = "Professor"
    elif designation.startswith("D") or designation.startswith("d") :
        designation = "Dean"
    elif designation.endswith("F") or designation.endswith("f") :
        designation = "Staff"
    elif designation.endswith("D") or designation.endswith("d") :
        designation = "Student"
    
    return formatted_name, designation, willingness

check_for_trip = input("Do you want to check payable amount for the trip: ")
if check_for_trip.startswith("Y") or check_for_trip.startswith("y") :
    cont = True
    while cont :
        input_check = False
        full_name = input("Enter your full name: ")
        while not input_check :
            if (full_name.__contains__(" ")) :
                input_check = True
            else :
                full_name = input("Enter your full name with space(s): ")

        designation = input("Enter your position: ")

        input_check = False
        start_date = input("Enter your start date as DD.MM.YYYY: ")
        while not input_check :
            if len(start_date) == 10 :
                day = start_date[0:2]
                month = start_date[3:5]
                year = start_date[6:10]
                if day.isdigit() and month.isdigit() and year.isdigit() :
                    day = int(day)
                    month = int(month)
                    year = int(year)

                    if 1 <= day <= 31 and 1 <= month <= 12 and 1993 <= year <= 2023:
                        input_check = True

            if not input_check :
                start_date = input("Invalid. Enter the start date in correct format: ")

        wilingness = input("Would you like to partipicate in event: ")
        full_name, designation, wilingness = format_data(full_name, designation, wilingness)

        price = calculate_price(designation, start_date, wilingness)
        print()
        print("The Details of individual are:")
        print("Name = ", full_name)
        print("Position = ", designation)
        print("Start Year = ", year)
        print("Willingness = ", wilingness)
        print("The individual's expenditure will be ", price, " USD.")
        print()

        check_for_trip = input("Do you want to check for someone else: ")
        if not check_for_trip.startswith("y") and not check_for_trip.startswith("Y") :
            cont = False

print("Have a good day!")

