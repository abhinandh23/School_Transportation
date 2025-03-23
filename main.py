from database import MYSQLconnectionCheck, MYSQLconnection
from operations import new, display, update
from about import about

myConnection = MYSQLconnectionCheck()
if myConnection:
    myConnection = MYSQLconnection()
    about()
    while True:
        print()
        print("+----------------------------------------------+")
        print("|                    CHOICES                   |")
        print("+----------------------------------------------+")
        print("|                                              |")                                        
        print("|        1 - DISPLAY SCHOOL TRANSPORT DATA     |")
        print("|        2 - INSERT A NEW DATA                 |")
        print("|        3 - MODIFY THE BUS NO.                |")
        print("|        4 - EXIT                              |")
        print("+----------------------------------------------+")
        print("\n")
        
        choice = int(input("PLEASE ENTER YOUR CHOICE :"))
        if choice == 1:
            display(myConnection)
        elif choice == 2:
            new(myConnection)
        elif choice == 3:
            update(myConnection)
        elif choice == 4:
            myConnection.close()
            break
        else:
            print(" SORRY, MAYBE YOU ARE ENTERING WRONG INPUT, PLEASE TRY AGAIN !!!")
else:
    print("CHECK YOUR MYSQL CONNECTION FIRST !!!")
