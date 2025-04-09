#List and tuple assignment

import csv

def displayMenu():                                          #Gives menu options
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")
    
    userPick = input("Choice: ")                    #Gets user input
    return int(userPick)          

def sortData(customer_info, tupindex):                  #Sorts the data in the file
    customer_info.sort(key=lambda tup: tup[tupindex])
        
def readData(fileName):
    customer_info = []          #Starts off as empty list

    with open('customers.txt', 'r') as file:
        csv_reader = csv.reader(file)
    
        next(csv_reader)        #Skips header row
    
        for row in csv_reader:
            customer = (row[1],row[2],row[9])   #The indexs that captures company name, contact name,and # number
            customer_info.append(customer)      #Add to the empty list
    return customer_info

def printData(customer_info):
    for tup in customer_info:                   #Prints the data
        print(tup)
        
def searchInfo(customer_info, search_category, tupindex):         #Used parameterization to make search into one function  
    userInput = input("Please enter " + search_category + " Name: ")        
    
    for customer_info in customer_info:
        if userInput == customer_info[tupindex]:
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
            sortData(customer_info,0)
            printData(customer_info)
        elif userPick == 2:
            sortData(customer_info,1)
            printData(customer_info)
        elif userPick == 3:
            print("Searching customer by company name...")
            searchInfo(customer_info, 'Company', 0)          
        elif userPick == 4:
            print("Searching customer by contact name...")
            searchInfo(customer_info, 'Contact', 1)
        elif userPick == 5:
            print("Quiting")
        else:
            print("Please try again")    
    
if __name__ == "__main__":
    main()