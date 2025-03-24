# file processing assignment

userInput = ''

while userInput !='q':
    userInput = input("Please enter a name or press 'q' to quit: ")
    if userInput =='q':
        break
    
    with open('names.txt', 'r') as file:
        found = False
                        
        for line in file:
        
            if line.strip() == userInput:
                print("This name is in the file")
                found = True
                break
        
        if not found:
            with open('nofound.txt', 'a') as file:
                file.write(userInput + "\n")
                print(f"This name'{userInput}'was not found")