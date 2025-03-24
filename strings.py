#strings assignment


from typing import Any


def printRLE(strSource):  # Run-length function
    rv = ''
    n = len(strSource)
    i = 0
    while i < n:  # Counts occurrences of current character
        if strSource[i] == '#':  # If we encounter '#'
            if i + 1 < n and strSource[i + 1] == '#':  # Check if it's part of an escape sequence
                rv += "##"  # Add the escaped '##'
                i += 2  # Skip the next '#' character
            else:
                rv += "#"  # Just add a single '#'
                i += 1  # Move to the next character
        else:  # For other characters (non '#')
            count = 1
            # Count consecutive occurrences of the same character
            while i + 1 < n and strSource[i] == strSource[i + 1]:
                count += 1
                i += 1  # Move to the next character
            rv += strSource[i] + str(count)  # Add the character first, then the count
            i += 1  # Move to the next character

    return rv    

def decodingRLE(strSource):
    rv = ''                  
    printL = ''              
    n = len(strSource)       
    i = 0                    
    number = ''              
    
    while i < n:  # This while loop counts up the string
        currentLet = strSource[i]
        
        # Check for the escape sequence '##' (two '#' characters)
        if currentLet == '#':
            if i + 1 < n and strSource[i + 1] == '#':  # Found '##'
                rv += "#"  # Treat '##' as a literal '#'
                i += 2  
            else:  
                rv += "#"  # Treat it as a normal '#'
                i += 1
        elif not currentLet.isdigit():  # Checks if it's not a digit (i.e., a letter)
            if number == '':  # In case the letter doesn't have a number after it, we assume it's 1
                number = '1'
            rv = rv + printL * int(number)  # Adds the current character with the count
            number = ''  # Reset the number for the next character
            printL = currentLet  # Set the current character
        else:  # If it's a digit, accumulate the number
            number += currentLet           
        i += 1    
    if number == '': 
        number = '1'
    
    rv = rv + printL * int(number)  # Add the last character with its count
    
    return rv           
            
def main():
    strSource = input("Please enter a string of alphabetic letters: ")      #Prompt the user
    answer = ''
    if any(char.isdigit() for char in strSource):       #Check's to see if the string needs to be decoded or incoded         
        answer = decodingRLE(strSource)
    else:        
        answer = printRLE(strSource)
    print(answer)
    print()
        
if __name__ == "__main__":
    main()