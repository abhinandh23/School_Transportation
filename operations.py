def new(myConnection):
    if myConnection:
        cursor = myConnection.cursor()
        c = int(input("\n ENTER ADMISSION NUMBER:"))
        d = input("\n ENTER STUDENT NAME:")
        e = input("\n ENTER BUS STOP:")
        f = int(input("\n ENTER BUS NO.:"))
        
        sql = "INSERT INTO sts VALUES(%s, %s, %s, %s)"
        values = (c, d, e, f)
        cursor.execute(sql, values)
        myConnection.commit()
        cursor.close()
        print("\n NEW DATA HAS BEEN UPDATED")
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION")

def display(myConnection):
    if myConnection:
        cursor = myConnection.cursor()
        cursor.execute("SELECT * FROM sts")
        data = cursor.fetchall()
        print('-'*100)
        print('%10s'%'ADM_NO','%19s'%'STUD_NAME','%25s'%'BUS_STOP','%20s'%'BUS_NO')
        print('-'*100)
        for row in data:
            print('%10s'%row[0],'%19s'%row[1],'%25s'%row[2],'%20s'%row[3])
        print('-'*100)
        cursor.close()
    else:
        print("\n SOMETHING WENT WRONG, PLEASE TRY AGAIN")

def update(myConnection):
    if myConnection:
        cursor = myConnection.cursor()
        a = input("\n ENTER THE ADMISSION NUMBER :")
        cursor.execute(f'SELECT * FROM sts WHERE ADM_NO={a}')
        data = cursor.fetchall()
        if not data:
            print('ADMISSION NUMBER NOT FOUND, PLEASE TRY AGAIN...!!!')
        else:
            b = input("\n ENTER THE NEW BUS NUMBER :")
            z = input("Data will be changed permanently! Are you sure(Y/N)?")
            if z.lower() == 'y':
                sql = "UPDATE sts SET BUS_NO=%s WHERE ADM_NO=%s"
                values = (b, a)
                cursor.execute(sql, values)
                myConnection.commit()
                print("\n DATA UPDATED SUCCESSFULLY")
            else:
                print("UPDATE FUNCTION ABORTED")
        cursor.close()
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION")
