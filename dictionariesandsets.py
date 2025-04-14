#Dictionaries and sets assignment
import csv

def readData(fileName):
    customer_info = []          #Starts off as empty list

    with open(fileName, 'r') as file:
        csv_reader = csv.reader(file)
    
        next(csv_reader)        #Skips header row
        
        for row in csv_reader:
            customer = {'CompanyName': row[1] ,'ContactName': row[2], 'Phone': row[9]}
            customer_info.append(customer)      #Add to the empty list
    return(customer_info)

def sortData(customer_info, dictindex):                  #Sorts the data in the file
    return sorted(customer_info, key=lambda dict: dict[dictindex])
    
def printData(customer_info):
    for customer in customer_info:                   #Prints the data
        print(customer)

def displayMenu():                                          #Gives menu options
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")
    
    userPick = input("Choice: ")                    #Gets user input
    return int(userPick)


def searchInfo(customer_info, search_category, dictindex):         #Used parameterization to make search into one function  
    userInput = input("Please enter " + search_category + " Name: ")        
    
    for customer_info in customer_info:
        if userInput == customer_info[dictindex]:
            print(customer_info)
            return 
    print(search_category + "Name: " + userInput + " Not found")

def main():
    userPick = ''                       
    fileName = 'customers.txt'
    customer_info = readData(fileName)
    
    while userPick != 5:                #Logic for the menu
        userPick = displayMenu()
        if userPick == 1:           
            print("Sorting by company name")
            sortData(customer_info,'CompanyName')
            printData(customer_info)
        elif userPick == 2:
            print("Sorting by contact name")
            sortedcustomers = sortData(customer_info,'ContactName')
            printData(sortedcustomers)
        elif userPick == 3:
            print("Searching customer by company name...")
            searchInfo(customer_info, 'Company', 'CompanyName')
        elif userPick == 4:
            print("Searching customer by contact name...")
            searchInfo(customer_info, 'Contact', 'ContactName')
        elif userPick == 5:
            print("Quiting")
        else:
            print("Please try again")    
    
if __name__ == "__main__":
    main()