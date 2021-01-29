# Program to calculate BMI for pands Lab 2.2
# Author: Gerry Donnelly
# Program takes Height and Weight inputs from the user and outputs the BMI score and indicates if Low, Normal or High


H = int(input("Please enter your height in CM: "))
W = int(input("Please enter your weight in KG: "))
BMI = W/((H/100)*2) # Calculate the BMI
if BMI<18.5: # Check if it is low
    print ("Your BMI is " + str(BMI) + " and is LOW ")
elif BMI>25:
        print ("Your BMI is " +  str(BMI) + " and is HIGH") #Check if it is High
else: 
    print ("Congrats Your BMI is " + str(BMI) + " and is NORMAL ")# If not Low or High then it is Nornal. 
