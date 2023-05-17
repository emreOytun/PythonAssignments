import random

random.seed(100)

def roll_biased_die() :
    randomNum = random.randint(1, 100);
    result = 0
    if (1 <= randomNum and randomNum <= 10) :
        result = 1
    elif (11 <= randomNum and randomNum <= 30) :
        result = 2
    elif (31 <= randomNum and randomNum <= 60) :
        result = 3
    elif (61 <= randomNum and randomNum <= 75) :
        result = 4
    elif (76 <= randomNum and randomNum <= 85) :
        result = 5
    else :
        result = 6

    print(result, " has been rolled")
    return result

def play_round(playerName) :
    print(playerName, "'s turn:")
    
    # Initialize type with -1 for now.
    type = -1

    # If player is the user, get input type indicating odd or even.
    if (playerName != "Computer") :
        type = int(input("Choose odd or even for this round(0/1): "))
        while (type != 0 and type != 1) : 
            type = int(input("Invalid choice. Choose either even or odd (0/1): "))
    else :     
        type = random.randint(0,1);
        if (type == 0) :
            print("Computer chose even.")
        else :
            print("Computer chose odd.")

    
    # Roll the die
    die1 = roll_biased_die()
    die2 = roll_biased_die()
    die3 = roll_biased_die()

    score = die1 + die2 + die3
    if ((die1 == 6 and die2 == 6) or (die1 == 6 and die3 == 6) or (die2 == 6 and die3 == 6)) :
        print("Double Sixes!", playerName, "'s score for this round is 0.")
        score = 0
    else :
        if (die1 + die2 + die3 == 12) :
            print("Lucky Twelve!", playerName, "'s score for this round is increased by 12.")
            score += 12
        if (type == 0 and die1 % 2 == 1 and die2 % 2 == 1 and die3 % 2 == 1) :
            print("All roles are odd!", playerName, "'s score for this round is increased by 15.")
            score += 15
        elif (die1 % 2 == 0 and die2 % 2 == 0 and die3 % 2 == 0) :
            print("All roles are even!", playerName, "'s score for this round is increased by 15.")
            score += 15
    
    print(playerName, "'s score for this round: ", score)
    return score

def play_game() :
    playerName = input("Enter the name of the user: ")
    userTotalScore = 0
    computerTotalScore = 0

    roundNum = 1
    while (roundNum != 6) :
        print()
        print("Round ", roundNum)
        userScore = play_round(playerName)
        computerScore = play_round("Computer")
        if (userScore == computerScore) :
            print("Round ", roundNum, " is a tie! Replay the round.")
        elif (userScore > computerScore) :
            print(playerName, " wins round ", roundNum, "!")
            userTotalScore += 1
            roundNum += 1
        else :
            print("Computer wins round " , roundNum, "!")
            computerTotalScore += 1
            roundNum += 1
            
    if (userTotalScore > computerScore) :
        print(playerName, "  wins the game with ", userTotalScore, " rounds won!")
    else :
        print("Computer wins the game with  ", computerTotalScore, " rounds won!")

play_game()