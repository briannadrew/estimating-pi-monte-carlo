# assignment1_q3.py

# Brianna Drew
# January 20, 2021
# ID: #0622446
# Assignment #1, Question #3

# import required modules
import random
import math
import time
import matplotlib.pyplot as plot

run = True
pi = math.pi
pi_digits = [] # list to hold digits after radix point of pi
scatter_x = [] # list to hold items of x-axis of scatter plot
scatter_y = [] # list to hold items of y-axis of scatter plot
counter = 0 # counter to iterate and add to lists

# add digits after the radix point of the value of pi to a list
for digit in str(pi):

    #skip the first digit and the radix point
    if counter > 1:
        pi_digits.append(int(digit))

    counter += 1

# run this until the user no longer wants to generate more points
while run:

    inside = 0 # counter for points that are inside the circle
    outside = 0 # counter for points that are outside the circle
    inputCheck = True # boolean to validate input or not

    # while loop will run until user input is valid
    while inputCheck:

        # receive number of points to generate from user
        iterations = input("Please enter the number of iterations that should be performed to estimate the value of pi: ") 

        # if the user entered a valid positive integer...
        if iterations.isdigit():
            # convert user inputted string to integer
            iterations = int(iterations) 

            # 0 iterations also would not make sense
            if iterations == 0: 
                print("Invalid number. Please try again...")
                # immdediately continue to next iteration of while loop
                continue 

            # exit loop
            inputCheck = False

        # if the user entered an invalid positive integer...
        else:
            print("Invalid number. Please try again...")

    # seed the random number generator
    random.seed(int(round(time.time()*1000)))

    for i in range(iterations):

        # generate two random numbers from 0 to 1
        x = random.random()
        y = random.random()
    
        # calculate distance from origin
        dist = math.sqrt((x*x) + (y*y))
   
        # determine whether the point is inside or outside the circle
        if dist < 1 :
            # increment counter for inside
            inside += 1

        else:
            # increment counter for outside 
            outside += 1

    # calculate the estimated value of pi 
    pi_est = (inside / iterations) * 4

    # print result
    print("RESULTS:")
    print("--------")
    print("Iterations: ", iterations, ", Pi Estimation: ", pi_est,
        ", Actual value of Pi: ", pi, ", Difference: ", abs(pi - pi_est))

    pi_est_digits = [] # list to hold digits after radix point of estimated value of pi
    counter = 0

    # add digits after the radix point of the estimated value of pi to a list
    for digit in str(pi_est):

        #skip the first digit and the radix point
        if counter > 1:
            pi_est_digits.append(int(digit))
            
        counter += 1

    # determine which of the actual value of pi or the estimated value of pi is shorter and get it's length
    if len(pi_est_digits) >= len(pi_digits):
        length = len(pi_digits)
        shorter = pi_digits
        longer = pi_est_digits
    else:
        length = len(pi_est_digits)
        shorter = pi_est_digits
        longer = pi_digits

    # add digits of the longer number to the list containing the digits of the shorter number (only as many digits as the shorter one)
    for digits in range(length):
        shorter.append(longer[digits])

    correct = 0 # count how many digits of pi were correctly estimated
    long_count = length

    # compare each digit of pi with the corresponding digit of the estimated value of pi to determine equality or lack thereof
    for short_count in range(length):
        if shorter[short_count] == shorter[long_count]:
            correct += 1
        long_count += 1

    # x-axis of scatter plot = # of iterations    
    scatter_x.append(iterations)
    # y-axis of scatter plot = # of correctly estimated digits of pi (after radix point)
    scatter_y.append(correct)

    inputCheck = True

    # while loop will run until user input is valid
    while inputCheck:

        # receive response from user
        response = input("Would you like to run the program again? Type 1 for yes, type 0 for no: ")

        # if user does not want to generate more points...
        if response == "0":
            run = False
            inputCheck = False

        # if the user wants to generate more points...
        elif response == "1":
            inputCheck = False

        # if the user's response is invalid
        else:
            print("Invalid response. Please try again...")

# create and display the scatter plot
plot.scatter(scatter_x, scatter_y)
plot.title("Estimating Pi with the Monte Carlo Approach")
plot.xlabel("Iterations")
plot.ylabel("Correctly Estimated Digits (after radix point)")
plot.savefig("assignment1_scatterplot.png")
plot.show()