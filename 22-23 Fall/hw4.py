
isDone = False
tryCount = 0
while (not isDone) :
    isRead = True
    try:
        password = int(input("Enter password : "))
    except ValueError:
        isRead = False
    
    if isRead and password == 1234 :
            isDone = True
    else :
        print("Invalid password.")
        tryCount += 1
        if tryCount == 3 :
            tryCount = 0
            isRecoveryCodeTaken = False
            while (not isRecoveryCodeTaken) :
                isRead = True
                try:
                    recoveryCode = int(input("Enter a recovery code : "))
                except ValueError :
                    isRead = False
                
                if not isRead :
                    print("Invalid recovery code.")

                elif recoveryCode <= 0 :
                    print("Enter a positive number.")

                else :
                    digitSum = 0
                    while not (recoveryCode / 10 == 0) :
                        digitSum += (int) (recoveryCode % 10)
                        recoveryCode /= 10
                        
                    if digitSum % 11 == 0 :
                        isRecoveryCodeTaken = True

curScreen = 0
isDone = False
while (not isDone) :
    print("Current screen is: " + str(curScreen))
    isRead = True
    try :
        command = int(input("Enter screen command : "))
    except ValueError :
        isRead = False
    
    if not isRead :
        print("Enter a valid command.")

    elif command == 1 :
        if curScreen == 2 :
            curScreen = -2
        else :
            curScreen += 1

    elif command == 2 :
        if curScreen == -2 :
            curScreen = 2
        else : 
            curScreen -= 1
     
    elif command == 3 :
        print("Screen is closed.")
        isDone = True

    else :
        print("Enter a valid command.")
