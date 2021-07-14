import mysql.connector
from mysql.connector import MySQLConnection, Error

myconnection = mysql.connector.connect(host="localhost", user="root", password="root", database="db")
mycursor = myconnection.cursor()
print("""Please enter any choice 
L FOR LOGIN
R FOR  REGISTER
A FOR ADMIN LOGIN
Q FOR QUIT THE MENU""")
choice = input("Enter your choice = :: ")

if myconnection.is_connected():

    print("connection is sucessful")
    if choice == 'L':
        name = input('Enter Name :: ')
        pwd = input("Enter password :: ")
        sql = "select name from reg where name='"+name+"' and password ='"+pwd+"' "
        mycursor.execute(sql)
        record = mycursor.fetchall()
        if len(record)>=1:


            #add the user name
            print("Log in successful Welcome to the Garbage management system Mr",record[0][0],"Please recharge your account ")
            print("""1.GARBAGE
2.UPDATE DETAIL 
3.VIEW DETAIL""")
            data = int(input("enter any choice  : "))
            if data== 1:
                waste = input("Do you want to dump waste yes (y) No(n): ")
                if waste == 'y':
                    print("Please select any options ")
                    print("""1. DRY
2. WET""")
                    category = int(input("ENTER THE CATEGORY OF GARBAGE :"))
                    if category == 1:
                        price= 20
                        sql ="SELECT Balance FROM reg WHERE name='"+name+"'"
                        mycursor.execute(sql)
                        recordbal=mycursor.fetchall()
                        wamt = int(input("Please enter quantity :"))
                        if (price*wamt)<=recordbal[0][0]:
                            abal= str(recordbal[0][0]-price*wamt)
                            sql = ("UPDATE reg SET Balance='" + abal + "' WHERE name= '" + name + "'")
                            mycursor.execute(sql)
                            myconnection.commit()
                            print("Hello we will come to your place and collect it soon")
                            #print("Hello", record[i][0], " we will come to your place and collect it soon")
                            # print(record[i][0],"your charges for service is : ", (price*wamt)," and your current balance is",abal)
                            print(record[0][0],"your charges for service is : ", (price * wamt),
                                  " and your current balance is", abal)

                        else:
                            print("Insufficient Balance Mr",record[0][0])



                    elif category==2:
                                    #write logic for wet garbage
                        price = 10
                        sql = "SELECT Balance FROM reg WHERE name='" + name + "'"
                        mycursor.execute(sql)
                        recordbal = mycursor.fetchall()
                        wamt = int(input("Please enter quantity (eg. 1,2,3):"))
                        if (price * wamt) <= recordbal[0][0]:
                            abal = str(recordbal[0][0] - price * wamt)
                            sql = ("UPDATE reg SET Balance='" + abal + "' WHERE name= '" + name + "'")
                            mycursor.execute(sql)
                            myconnection.commit()
                            print("we will come to your place and collect it soon")
                            # print("Hello", record[i][0], " we will come to your place and collect it soon")
                            # print(record[i][0], "your charges for service is : ", (price * wamt),and your current balance is", abal)

                            print("your charges for service is : ", (price * wamt)," and your current balance is", abal)
                                # break
                        else:
                            print("Insufficient Balance")
                            # print("Insufficient Balance Mr",record[i][0])

                    else:
                        print("Please select a valid options")
                                # print("Hello", record[i][0], " we will come to your place and collect it soon")
                                # write logic for options dry or wet garbage
                                # set price for both dry and wet garbage
                           # check if user has available balance or not
                                # if yes deduct the amount if not du
                                #

                            # break
                elif waste == 'n':
                    print("Thanks for your response ")
                        # break
                else:
                    print("please select only y or n only")
                        # break

            elif data==2:
                mobileno = input('Enter mobile no:')
                emailid = input('Enter Email-Id:')
                #Logic without the DATABASE

                update = {"mobileno" : mobileno,
                          "emailid"  : emailid}

                update.Update({"mobileno" :mobileno})
                update.Update({"emailid" : emailid})
                print(update)

                sql = "UPDATE reg SET mobileno='" + mobileno + "',emailid ='"+emailid+"' WHERE name= '" + name + "'"
                mycursor.execute(sql)
                myconnection.commit()
                r= mycursor.fetchall()
                print(r)
                print(mycursor.rowcount, "value updated.")
            elif data==3:
                sql = "SELECT * FROM reg WHERE name='" + name+ "'"
                mycursor.execute(sql)
                record = mycursor.fetchall()
                print(record[0])
                print("value retrieved ")

            elif data==4:
                pass
            else:

                print("please enter the value between 1-4")
        else:
    # #if not match with database then.....
            print("Invalid credential ")
            print("1. REGISTER")
            print("2. QUIT")
            c = input("Please enter your choice 1,2:")
            if c=='1':
                name = input('Enter Name:')
                address = input('Enter addd :')
                mobileno = input('Enter mobile no :')
                emailid = input('Enter Email-Id:')
                house_no = input("enter your house no : ")
                ward_no = input("enter your ward no : ")
                garbage_qty = input("enter your garbadge qty : ")

                sql = "INSERT INTO reg  VALUES ('" + name + "','" + address + "','" + mobileno + "','" + emailid + "','" + house_no + "','" + ward_no + "','" + garbage_qty + "')"
                mycursor.execute(sql)
                myconnection.commit()
                print(mycursor.rowcount, "value inserted.")

            elif c=='2':
                pass
            else:
                print("please enter valid options")
    elif choice=='R':
        # Write logic for Register
        name = input('Enter Name:')
        address = input('Enter addd :')
        mobileno = input('Enter mob'
                         'ile no :')
        emailid = input('Enter Email-Id:')
        house_no = input("enter your house no : ")
        ward_no = input("enter your ward no : ")
        garbage_qty = input("enter your garbadge qty : ")
        balance = input("please enter your balance: ")
        password = input("enter your password :: ")

        #logic without database
        register = {"name": name,
                    "address": address,
                    "mobileno" : mobileno,
                    "emailid" : emailid,
                    "houseno" : house_no,
                    "wardno" : ward_no,
                    "garbageqty" :  garbage_qty,
                    "balance"    : balance,
                    "password"   : password}
        register.update({"name" : name})
        register.update({"address": address})
        register.update({"address" : address})
        register.update({"mobileno" : mobileno})
        register.update({"emailid" : emailid})
        register.update({"houseno" : house_no})
        register.update({"wardno" : ward_no})
        register.update({"garbageqty" :  garbage_qty})
        register.update({"balance" : balance,})
        register.update({"password" : password})
        print(register)

        sql = "INSERT INTO reg  VALUES ('" + name + "','" + address + "','" + mobileno + "','" + emailid + "','"+house_no+"','"+ward_no+"','"+garbage_qty+"','"+balance+"','"+password+"')"
        mycursor.execute(sql)
        myconnection.commit()
        print(mycursor.rowcount, "value inserted.")
                #break
    elif choice=='A':
        # write logic for admin login
        print("Chose the operation to do :: ")
        print("1. Delete User by Username ")
        print("2. Update Information ")
        print("3.View the Detail")
        ainput= int(input("please enter any choice : "))


        # Delete the Row

        if ainput == 1:
            namevar= input("enter the name  to delete: ")
            sql = "DELETE FROM reg WHERE name ='"+namevar+"'"
            mycursor.execute(sql,namevar)
            myconnection.commit()
            print("deleted row successfully")

        # Update the table
        elif ainput == 2:
            nameold = input("Enter the Name to Update :: ")
            namenew = input('Enter Name :: ')
            address = input('Enter Address :: ')
            mobileno = input('Enter Password :: ')
            emailid = input('Enter Email-Id :: ')
            garbage_qty = int(input("Enter your Garbadge Qty :: "))

            #UPDATING WITHOUT DB
            # update = {"mobileno": mobileno,
            #           "emailid": emailid}
            #
            # update.Update({"mobileno": mobileno})
            # update.Update({"emailid": emailid})
            # print(update)

            sql = "UPDATE reg SET name='" + namenew + "',address='" + address + "',mobileno='" + mobileno + "',emailid='" + emailid +"',garbageqty='"+garbage_qty+"', WHERE name= '"+nameold+"'"
            mycursor.execute(sql)
            myconnection.commit()
            print(mycursor.rowcount, "value updated.")

        #views the details
        elif ainput == 3:

            n = input("enter name to show detail")
            sql = "SELECT * FROM reg WHERE name='"+n+"'" # withot error it running correctly
            mycursor.execute(sql,n)
            record = mycursor.fetchall()
            print(record)
            print( "value retrieved ")
                #CREATE THE USER
        elif ainput==4:
            print("Write logic for user creations ")
        else:
            print("please enter a valid options")
                #break
    elif choice=='Q':
        print("write logic for QUIT")
                #break

    else:
        print("please enter a valid choice")
else:
    print("connection is not connected")
    mycursor = myconnection.cursor()

if myconnection.is_connected():
    mycursor.close()
    myconnection.close()
    print("MySQL connection is closed")









