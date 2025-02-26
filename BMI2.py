#BMI 

def getUser():
    while True:
        try:
            weight = input("Please enter your weight in lbs: ") #Prompt the user to get their weight
            if weight == 'q':                                   #Check if its q, if it is then end program
                exit()
            else:                                               #If not check if its valid input
                intweight = int(weight)
                if intweight < 0:
                    raise ValueError           
            break
        except ValueError:
            print("This is a invalid input. Please try again.")
    
    while True:
        try:
            heightF = input("Please enter your height in feet: ") #Prompt the user get their height in feet
            if heightF == 'q':
                exit()
            else:
                intheightF = int(heightF)
                if intheightF < 0:
                    raise ValueError
            break
        except ValueError:
           print("This is a invalid input. Please try again.") 
        
    while True:
        try:
            heightIn = input("Please enter your inches: ")      #Prompt the user to get the left over height in inches
            if heightIn == 'q':
                exit()
            else:
                intheightIn = int(heightIn)
                if intheightIn < 0:
                    raise ValueError
                
            heightT = intheightF * 12 + intheightIn   #Gets a total height by converting the feet to inches and adding the two
            break
        except ValueError:
            print("This is a invalid input. Please try again.")
            
    return intweight, heightT

def calculateBMI(weight,heightT): #Calculates the BMI by using the BMI Formula
    if heightT <= 0:
        raise ValueError("Height can't be 0 or negative.")
    if weight <= 0:
        raise ValueError("weight can't be 0 or negative.")
    BMI = (weight / (heightT * heightT)) * 703
    return BMI
    ##print(BMI)
    
def displayRanges():        #Just displays the ranges of weight
    print("Underweight: <18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25>")
    
def displayTable():             #Displays the table
    print("The BMI table")
    print(end= "     ")         #Spacing
    
    for curheight in range (58, 76, 2):     #Loop to create the column on the top
        print(curheight, end= "     ")
    print()   
    for curweight in range (100, 250, 10):  #Loop to create the rows
        print(curweight, end= "  ")
        
        for curheight in range(58, 76, 2):
            BMI = calculateBMI(curweight,curheight)     #Creates the BMI in the table
            print(round(BMI,2), end= "  ")
        print()


def main():
    userInput = ''                          #Empty variable that helps with ending the code

    while userInput != 'q':                 #The condition to end the code
        userInput = input("Press q if you want to quit and any other key to continue: ") 
        if userInput !='q':       
            weight, heightT = getUser()
            bmi = calculateBMI(weight,heightT)   #Calling my functions
            print("Your BMI is:", round(bmi, 2))      
            displayTable()

if __name__ == "__main__":
    main()
