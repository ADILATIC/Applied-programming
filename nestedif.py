#assignment 3 #example of an exception

try:                                                                        #running our test
    number = int(input("Please enter a number that is between 0-100: "))        #prompt the user and get the users input
    
except ValueError:                                      #Check to see if datatype is correct   
    print("This is a invalid input.Please try again.")      

if number < 0 or number > 100:                          #Checking if the input is between 0 and 100
    print("The number is not between 0-100.")
else:                                                   #Otherwise show a success prompt
    print("Thank you for entering:", number)            
        