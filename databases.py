# Session 11 Database 

'''import sqlite3

conn = sqlite3.connect('Northwind.db')
c = conn.cursor()

def readTables():
    tables = []
    userInput = ""
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    for row in rows:
        tables.append(row[0])
    while True:
        print(tables)
        userInput = input("Please enter the table name you want to look into: ")
        if userInput in tables:
            return userInput
        else:
            print("Please try again")
        
def displayTable(userInput, columnNames):
    c.execute("Select * FROM {0}".format(userInput))
    rows = c.fetchall()
    rowNum = 1
    
    print("Row Number ", end= ' ')
    for column in columnNames:            #This loop is used to print the columns
        print(f"{column:<20}", end=' ')
    print()
    
    for row in rows:
        print(f"{rowNum:<12}", end=' ')
        rowNum +=1
        for index in range (len(columnNames)):
            value = str(row[index]) if row[index] is not None else ""
            print(f"{value:<20}", end=' ')
        print()

def insertTable():
    c.execute("INSERT INTO sqlite_master WHERE type='table';")    

def getColumnNames(userInput):
    rows = c.execute('Select * FROM {0}'.format(userInput))
    columnNames = list(map(lambda x: x[0], rows.description))
    return columnNames
     
userInput = readTables()
columnNames = getColumnNames(userInput)
displayTable(userInput, columnNames)
c.close()
conn.close()'''

import sqlite3

conn = sqlite3.connect('Northwind.db')
c = conn.cursor()

def readTables():
    tables = []
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    for row in rows:
        tables.append(row[0])     #Adds the tables to a list/tuple

    while True:                    #Prints out the avaible tables
        print("\nAvailable tables:")
        for table in tables:
            print(f" - {table}")
        userInput = input("\nEnter the table name to view: ") #Prompts the user
        if userInput in tables:
            return userInput
        else:
            print("Invalid table name. Please try again.")

def getColumnNames(userInput):  #This function gets the column names from the table
    c.execute(f"SELECT * FROM {userInput} LIMIT 1")
    return [description[0] for description in c.description]

def displayTable(userInput, columnNames):      #Displays the rows and information
    c.execute(f"SELECT * FROM {userInput}")
    rows = c.fetchall()
    rowNum = 1

    print("\nRow Number ", end=' ')
    for column in columnNames:
        print(f"{column:<20}", end=' ')
    print()

    for row in rows:
        print(f"{rowNum:<12}", end=' ')
        rowNum += 1
        for index in range(len(columnNames)):
            value = str(row[index]) if row[index] is not None else ""
            print(f"{value:<20}", end=' ')
        print()

def modifyTable(userInput, columnNames):   
    while True:    
        choice = input("Choose how to modify (I)nsert, (U)pdate, (D)elete, (Q)uit:").strip().upper()
            #.strip removes any spacing and .upper makes all lowercase entries uppercase
        if choice == 'I':
            insertTable(userInput, columnNames)
        elif choice == 'U':
            updateTable(userInput, columnNames)
        elif choice == 'D':
            deleteTable(userInput, columnNames)
        elif choice == 'Q':
            print("Quiting")
            break
        else:
            print("Invalid choice, try again")    

def insertTable(userInput, columnNames):
    values = []
    for col in columnNames:
        val = input(f"Please enter a value for {col}: ")
        values.append(val)
                
    cols = ", ".join(columnNames)
    placeholders = ", ".join(["?"] * len(columnNames))
    sql = f"INSERT INTO {userInput} ({cols}) VALUES ({placeholders})"
    
    c.execute(sql, values)
    conn.commit()
    print("Records have been inserted successfully")    
    
def updateTable(userInput, columnNames):
    displayTable(userInput, columnNames)

    try:
        row_id = input("\nEnter the ID (primary key) of the record you want to update: ")
        column_to_update = input(f"Which column do you want to update? {columnNames}: ")

        if column_to_update not in columnNames:
            print("Invalid column name.")
            return

        new_value = input("Enter the new value: ")

        # Build the UPDATE SQL statement (assumes first column is primary key)
        primary_key = columnNames[0]
        sql = f"UPDATE {userInput} SET {column_to_update} = ? WHERE {primary_key} = ?"

        c.execute(sql, (new_value, row_id))
        conn.commit()
        print("Record updated successfully.")

    except Exception as e:
        print("Update failed:", e)    

def deleteTable(userInput, columnNames):
    
    displayTable(userInput, columnNames)  # Show current table contents
    
    primaryKey = columnNames[0]
    delete_id = input(f"\nEnter the {primaryKey} of the record to delete: ")

    confirm = input(f"Are you sure you want to delete the record with {primaryKey} = {delete_id}? (Y/N): ")
    if confirm.strip().upper() == 'Y':
        sql = f"DELETE FROM {userInput} WHERE {primaryKey} = ?"
        c.execute(sql, (delete_id,))
        conn.commit()
        print("Record deleted successfully")
    else:
        print("Delete operation canceled") 
        
# Main flow
while True:
    userInput = readTables()
    if userInput.lower() == 'exit':
        break
    columnNames = getColumnNames(userInput)
    displayTable(userInput, columnNames)
    modifyTable(userInput, columnNames)