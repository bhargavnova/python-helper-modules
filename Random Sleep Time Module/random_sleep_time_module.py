# Module to generate random sleep time, and implement it in the loop

import time
import random

def random_time_sleep():

    startTime=int(input("Enter the lower time limit: "))            # Making user input the left hand limit of sleep time
    endTime=int(input("Enter the upper time limit: "))              # Making user input the right hand limit of sleep time
    countdown=int(input("Enter the number from which you want to start the countdown: "))               # Making user input the number from which they want to start the countdown
    countdown=countdown+1

    while countdown:                # While loop until the loop hits "0" as the countdown value
        timeLimit=random.randint(startTime,endTime)             # Generating random sleep duration everytime the loop countdown decreases by "1"
        countdown-=1

        countdownHrs=countdown//3600                    # Time conversion 
        timeLeft1=(countdown-(countdownHrs*3600))       # Time conversion
        countdownMin=timeLeft1//60                      # Time conversion
        countdownSec=(timeLeft1-(countdownMin*60))      # Time conversion
        
        if (countdown>3599):                            # Loop when countdown is greater than "1" hour
            if (countdownMin>9):
                if (countdownSec>9):
                    print("",countdownHrs, ":", countdownMin, ":", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
                else:
                    print("",countdownMin, ":0", countdownSec, ":", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
            elif (countdownSec>9):
                print("",countdownHrs, ":0" ,countdownMin, ":", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
            else:
                print("",countdownHrs, ":0",countdownMin, ":0", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")

        elif (countdown>59 and countdown<3600):         # Loop when countdown is less than "1" hour but greater than "1" minute
            if (countdownMin>9):
                if (countdownSec>9):
                    print("0:" ,countdownMin, ":", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
                else:
                    print("0:",countdownMin, ":0", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
            elif (countdownSec>9):
                print("0:0" ,countdownMin, ":", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
            else:
                print("0:", countdownHrs, countdownMin, ":0", countdownSec, "\t ->Time Duration: ", timeLimit, sep="")
        elif (countdown>9 and countdown<60):
            print("0:00:",countdown, "\t ->Time Duration: ", timeLimit, sep="")             # Loop when countdown is less than "1" minute but greater than "10" seconds
        else:
            print("0:00:0",countdown, "\t ->Time Duration: ", timeLimit, sep="")            # Loop when countdown is less than "10" seconds

        time.sleep(timeLimit)               # Calling "sleep" function in "time" module to specify the time limit every time the countdown decreases by "1"

        if (countdown==0):
            break