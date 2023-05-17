import random

isDone = False
while (not isDone) :
    print()
    seed = int(input("Enter seed or 0 to stop: "))
    print()
    random.seed(seed)
    
    if (seed == 0) :
        isDone = True
    else :
        goodAcorns = 0
        badAcorns = 0
        totalRottenAcorns = 0
        curTree = 0
        dayCompleted = False
        while (not dayCompleted) :
            acornPerTree = 0
            while ( acornPerTree != 4 and goodAcorns < 10 and (not (goodAcorns >= 5 and badAcorns == 4)) ) :
                acornType = random.randint(0, 1)
                acornPerTree += 1
                if (acornType == 1) :
                    print("Encountered a good acorn!")
                    goodAcorns += 1
                    badAcorns = 0
                elif (acornType == 0) :
                    badAcorns += 1
                    totalRottenAcorns += 1
                    print("Encountered a bad acorn! Consecutive bad acorns: ", badAcorns)
                    
            
            curTree += 1
            if acornPerTree == 4 :
                print("Trees finished: ", curTree, "Collected acorns: ", goodAcorns, "Rotten acorns: ", totalRottenAcorns)

            if (curTree == 5 or goodAcorns == 10) :
                dayCompleted = True
            elif (goodAcorns >= 5 and badAcorns == 4) :
                dayCompleted = True
            
            if (dayCompleted) :
                print("Going home for today. Trees visited: ", curTree, "Acorns collected: ", goodAcorns)   
        