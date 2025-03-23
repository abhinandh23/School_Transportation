import mysql.connector

userName = ""
password = ""

def MYSQLconnectionCheck():
    global userName, password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME:")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD:")

    myConnection = mysql.connector.connect(host="localhost", user=userName, passwd=password)
    if myConnection:
        print("\n CONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS A")
        cursor.execute('USE A')
        createTable = """
        CREATE TABLE IF NOT EXISTS sts(
            ADM_NO INT PRIMARY KEY,
            STUD_NAME VARCHAR(20),
            BUS_STOP VARCHAR(30),
            BUS_NO INT
        )"""
        cursor.execute(createTable)
        myConnection.commit()
        cursor.close()
        return myConnection
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION. CHECK USERNAME AND PASSWORD")
        return None

def MYSQLconnection():
    global userName, password
    myConnection = mysql.connector.connect(host="localhost", user=userName, passwd=password, database="A")
    if myConnection:
        return myConnection
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION!")
        return None
