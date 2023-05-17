import math

earth_gravity = 9.807
orbit_constant = 2.5

def validate(value, lowerLimit, upperLimit) :
    isDone = False
    isRead = True
    while not isDone :
        if isRead and lowerLimit <= value and value <= upperLimit :
            isDone = True
        else :
            isRead = True
            try:
                print("You have entered an invalid value.")
                value = int(input("Please enter again: "))
            except ValueError:
                isRead = False

    return value

def launch_velocity(spaceCraft_t, cargoPayload, crewCapacity) : 
    if (spaceCraft_t == 1) :   
        num = (35000 + cargoPayload + (crewCapacity * 80))
        denom = (earth_gravity * math.sqrt(30))
        return 60.2 * (num / denom)
    else :
        num = (65000 + cargoPayload + (crewCapacity * 100))
        denom = (earth_gravity * math.sqrt(60))
        return 50.7 * (num / denom) 

def mission_duration(launchVelocity) : 
    num = float(orbit_constant * 384400)
    return num / launchVelocity


# Read space craft type.
isDone = False
spaceCraft_t = 0
while not isDone : 
    isRead = True
    try:
        spaceCraft_t = int(input("Please enter the type of the spacecraft [Orion: 1/Hermes: 2]: "))
        if (spaceCraft_t == 1 or spaceCraft_t == 2) :
            isDone = True
        else :
            print("Invalid spacecraft type.")
    except ValueError:
        print("Invalid input.")

cargoPayload = 0
isDone = False
while not isDone : 
    try:
        cargoPayload = int(input("Please enter the cargo payload: "))
        if (spaceCraft_t == 1) :
            cargoPayload = validate(cargoPayload, 20, 100)
        else :
            cargoPayload = validate(cargoPayload, 40, 200)
        isDone = True  
    except ValueError:
        print("You have entered an invalid value. Please try again.")

crewCapacity = 0
isDone = False
while not isDone : 
    try:
        crewCapacity = int(input("Please enter the crew capacity: "))
        if (spaceCraft_t == 1) :
            crewCapacity = validate(crewCapacity, 2, 6)
        else :
            crewCapacity = validate(crewCapacity, 2, 10)
        isDone = True  
    except ValueError:
        print("You have entered an invalid value. Please try again.")

launchVelocity = launch_velocity(spaceCraft_t, cargoPayload, crewCapacity)
missionDuration = mission_duration(launchVelocity)

if (spaceCraft_t == 1) :
    print("Launch velocity of Orion spacecraft is " + str(launchVelocity) + " km/h.")
    print("Mission duration of Orion spacecraft is " + str(missionDuration) + " days.")
else : 
    print("Launch velocity of Hermes spacecraft is " + str(launchVelocity) + " km/h.")
    print("Mission duration of Hermes spacecraft is " + str(missionDuration) + " days.")