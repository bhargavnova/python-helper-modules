# Module to generate random sleep time, and implement it in the loop

import time
import random
import sys

def random_sleep_time():

    minTime=int(input("Enter the maximum time limit (in seconds): "))            # Making user input the left hand limit of sleep time
    maxTime=int(input("Enter the upper time limit (in seconds): "))              # Making user input the right hand limit of sleep time 
    randomTime=random.randint(minTime,maxTime)                                   # Choosing a random integer in between the time interval
    print("-> Sleeping for", randomTime, "Seconds")                              # Printing the random number chosen

    while randomTime:                                                            # While looping for random time generated
        print("-> Now, Sleeping for", randomTime, "Seconds", end="\r")           # Sleep timer
        time.sleep(randomTime)
        randomTime-=1

        if (randomTime==0):                                                      # Breaking the loop at soon as the timer hits 0
            break