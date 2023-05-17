import math

courtWidth = float(input("Enter the single court's width (m) : "))
courtLength = float(input("Enter the single court's length (m) : "))
backhandSpeed = float(input("Enter the Roger Federer's backhand speed (m/s) : "))

ballDistance = math.sqrt(pow(courtWidth, 2) + pow(courtLength, 2))
arrivalTime = ballDistance / backhandSpeed

print("The time for ball to reach is " + "%.10f" %arrivalTime + " seconds.")