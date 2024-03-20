#Using the PhoneBook database from program 139, write a program that will display the following menu. If the user selects 1, they should be able to view the entire phonebook. If they select 2, it should allow them to add a new person to the phonebook. If they select 3, it should ask them for a surname and then display only the records of people with the same surname. If they select 4, it should ask for an ID and then delete that record from the table. If they select 5, it should end the program. Finally, it should display a suitable message if they enter an incorrect selection from the menu. They should return to the menu after each action, until they select 5. 

import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names( 
 id integer PRIMARY KEY, 
 name text NOT NULL, 
 surname text NOT NULL, 
 phone_num text );""")

choice = int(input("Enter a number (1-5): "))

if(choice==1):
    cursor.execute("SELECT * FROM Names") 
    print(cursor.fetchall())
elif(choice==2):
    newID = input("Enter ID number: ") 
    newName = input("Enter name: ") 
    newSurname = input("Enter surname: ") 
    newPhone_num = input("Enter phone number: ") 
    cursor.execute("""INSERT INTO employees(id,name,surname,phone_num) 
    VALUES(?,?,?,?)""",(newID,newName,newSurname,newPhone_num)) 
    db.commit() 
elif(choice==3):
    pass
elif(choice==4):
    pass
elif(choice==4):
    pass
else:
    pass

cursor.execute("""INSERT INTO Names(id,name,surname,phone_num) 
 VALUES("1","Simon","Howels","01223 349752")""") 
db.commit()

cursor.execute("""INSERT INTO Names(id,name,surname,phone_num) 
 VALUES("2","Karen","Phillips","01954 295773")""") 
db.commit()

cursor.execute("""INSERT INTO Names(id,name,surname,phone_num) 
 VALUES("3","Darren","Smith","01583 749012")""") 
db.commit()

cursor.execute("""INSERT INTO Names(id,name,surname,phone_num) 
 VALUES("4","Anne","Jones","01323 567322")""") 
db.commit()

cursor.execute("""INSERT INTO Names(id,name,surname,phone_num) 
 VALUES("5","Mark","Smith","01223 855534")""") 
db.commit()

db.close()