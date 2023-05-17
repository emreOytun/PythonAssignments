import random
seed = 100
random.seed(seed)

def roll_biased_die() :
    number = random.randint(1, 100);
    die = 1
    if number >= 1 and 10 >= number :
        die = 1
    elif number >= 11 and 30 >= number :
        die = 2
    elif number >= 31 and 60 >= number :
        die = 3
    elif number >= 61 and 75 >= number :
        die = 4
    elif number >= 76 and 85 >= number :
        die = 5
    else :
        die = 6
    print(die, " has been rolled")
    return die

def play_round(name) :
    print(name, "'s turn:")

    isOdd = 0
    if name == "Computer" :     
        isOdd = random.randint(0,1);
        if isOdd == 1 :
            print("Computer chose odd.")
        else :
            print("Computer chose even.")
   
    else :
        isOdd = int(input("Choose odd or even for this round(0/1): "))
        while isOdd != 0 and isOdd != 1 : 
            isOdd = int(input("Invalid choice. Choose either even or odd (0/1): "))
    
    die_1 = roll_biased_die()
    die_2 = roll_biased_die()
    die_3 = roll_biased_die()
    score = die_1+die_2 +die_3

    if die_1 == 6 and die_2 == 6 or die_1 == 6 and die_3 == 6 or die_2 == 6 and die_3 == 6 :
        print("Double Sixes!", name, "'s score for this round is 0.")
        score = 0
    else :
        if isOdd==0 and die_1%2 == 0 and die_2%2 == 0 and die_3%2 == 0 :
            score += 15
            print("All roles are odd!", name, "'s score for this round is increased by 15.")
        elif die_1%2 == 1 and die_2%2 == 1 and die_3%2 == 1 :
            score += 15
            print("All roles are even!", name, "'s score for this round is increased by 15.")

        if die_1+die_2+die_3 == 12 :
            score += 12
            print("Lucky Twelve!", name, "'s score for this round is increased by 12.")
        
    print(name, "'s score for this round: ", score)
    return score

def play_game() :
    name = input("Enter the name of the user: ")
    
    round = 1
    user_win = 0
    computer_win = 0
    
    while round < 6 :
        print()
        print("Round ", round)
        user_die = play_round(name)
        computer_die = play_round("Computer")
       
        if user_die > computer_die :
            user_win += 1
            print(name, " wins round ", round, "!")
            round += 1
            
        elif computer_die > user_die :
            computer_win += 1
            print("Computer wins round " , round, "!")
            round += 1

        else :
            print("Round ", round, " is a tie! Replay the round.")
        
    if user_win > computer_win :
        print(name, "  wins the game with ", user_win, " rounds won!")
    else :
        print("Computer wins the game with  ", computer_win, " rounds won!")

play_game()