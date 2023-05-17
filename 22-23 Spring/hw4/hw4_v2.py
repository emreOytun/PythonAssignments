import random

seed = -1
while (seed != 0) :
    print()
    seed = int(input("Enter seed or 0 to stop: "))
    print()
    random.seed(seed)
    
    if (seed != 0) :
        treeNumber = 0
        collectedAcorns = 0
        consecutiveBadAcorns = 0
        totalBadAcorns = 0
        while (treeNumber != 5 and collectedAcorns != 10 and not (consecutiveBadAcorns == 4 and collectedAcorns >= 5)) :
            acornCollected = 0
            while (acornCollected != 4 and collectedAcorns < 10 and not (consecutiveBadAcorns == 4 and collectedAcorns >= 5)) :
                isGoodAccorn = random.randint(0, 1)
                acornCollected += 1
                if (isGoodAccorn == 0) :
                    consecutiveBadAcorns += 1
                    totalBadAcorns += 1
                    print("Encountered a bad acorn! Consecutive bad acorns: ", consecutiveBadAcorns)
                else :
                    collectedAcorns += 1
                    consecutiveBadAcorns = 0
                    print("Encountered a good acorn!")

            treeNumber += 1
            if acornCollected == 4 :
                print("Trees finished: ", treeNumber, "Collected acorns: ", collectedAcorns, "Rotten acorns: ", totalBadAcorns)
        
        print("Going home for today. Trees visited: ", treeNumber, "Acorns collected: ", collectedAcorns)   
    
        