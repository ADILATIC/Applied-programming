#BMI group assignment

def getUser():
    weight = float(input("Please enter your weight in lbs: ")) #Prompt the user to get their weight
    heightF = float(input("Please enter your height in feet: ")) #Prompt the user get their height in feet
    heightIn = float(input("Please enter your inches: "))       #Prompt the user to get the left over height in inches
    
    heightT = heightF * 12 + heightIn   #Gets a total height by converting the feet to inches and adding the two
    return weight, heightT

def calculateBMI(weight,heightT): #Calculates the BMI by using the BMI Formula
    BMI = (weight / (heightT * heightT)) * 703
    print("Your BMI is:", end=" ")      #end= makes it so I can print twice on the same line
    print(BMI)
    
def displayRanges():        #Just displays the ranges of weight
    print("Underweight: <18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25>")

weight, heightT = getUser()
calculateBMI(weight,heightT)   #Calling my functions
displayRanges()