import mysql.connector
from mysql.connector import MySQLConnection, Error

print("hello")
print("""Please enter any choice 
========= L FOR LOGIN
========= R FOR  REGISTER
========= A FOR ADMIN LOGIN
========= Q for quit the Menu""")
choice = input("enter your choice = ")

try:
    myconnection = mysql.connector.connect(host="localhost", user="root", password="root", database="db")
    mycursor = myconnection.cursor()
    if myconnection.is_connected():
        print("connection is sucessful")
        #while choice == 'L' or choice == 'R' or choice =='A' or choice=='Q':
        if choice == 'L':
            if choice == 'L':
                name = input('Enter Name:')
                # addressvar = input("enter address")
                sql = "select name from reg"
                mycursor.execute(sql)
                record = mycursor.fetchall()

                i = 0
                while i < len(record):
                    if name in record[i]:
                        print("""Log in successful
=========================Welcome to the Garbage management system Mr""",record[i][0],"=========================")
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
                                        print("Hello", record[i][0], " we will come to your place and collect it soon")
                                        print(record[i][0],"your charges for service is : ", (price*wamt)," and your current balance is",abal)

                                    else:
                                        print("Insufficient Balance Mr",record[i][0])


                                elif category==2:
                                    #write logic for wet garbage
                                    price = 10
                                    sql = "SELECT Balance FROM reg WHERE name='" + name + "'"
                                    mycursor.execute(sql)
                                    recordbal = mycursor.fetchall()
                                    wamt = int(input("Please enter quantity :"))
                                    if (price * wamt) <= recordbal[0][0]:
                                        abal = str(recordbal[0][0] - price * wamt)
                                        sql = ("UPDATE reg SET Balance='" + abal + "' WHERE name= '" + name + "'")
                                        mycursor.execute(sql)
                                        myconnection.commit()
                                        print("Hello", record[i][0], " we will come to your place and collect it soon")
                                        print(record[i][0], "your charges for service is : ", (price * wamt)," and your current balance is", abal)
                                    else:
                                        print("Insufficient Balance Mr",record[i][0])




                                else:
                                    print("Please select a valid options")
                                # print("Hello", record[i][0], " we will come to your place and collect it soon")
                                # write logic for options dry or wet garbage
                                # set price for both dry and wet garbage
                           # check if user has available balance or not
                                # if yes deduct the amount if not du
                                #

                                break
                            elif waste == 'n':
                                print("Thanks for your response mr", record[i])
                                break
                            else:
                                print("please select only y or n only")
                                break

                        elif data==2:
                            mobileno = input('Enter mobile no:')
                            emailid = input('Enter Email-Id:')
                            sql = "UPDATE reg SET mobileno='" + mobileno + "', WHERE name= '" + name + "'"
                            mycursor.execute(sql)
                            myconnection.commit()
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
                    i = i + 1
                else:
                    print("Invalid credential ")
                    print("1. REGISTER")
                    print("2. QUIT")
                    c = input("Please enter your choice 1,2:")
                    if c=='1':
                        name = input('Enter Name:')
                        address = input('Enter addd :')
                        mobileno = input('Enter mobile no :')
                        emailid = input('Enter Email-Id:')
                        house_no = input("enter yo"
                                         "ur house no : ")
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
            print("Write logic for Register ")
            name = input('Enter Name:')
            address = input('Enter addd :')
            mobileno = input('Enter mobile no :')
            emailid = input('Enter Email-Id:')
            house_no = input("enter your house no : ")
            ward_no = input("enter your ward no : ")
            garbage_qty = input("enter your garbadge qty : ")
            balance = input("please enter your balance: ")

        #logic without database
            # register = {"name":
            #             "address": ,
            #             "mobileno" : ,
            #             "emailid" : ,
            #             "houseno" : ,
            #             "wardno" : ,
            #             "garbageqty" : ,
            #work in  progress
            #write dictonary in update section and save the data


            # }


            sql = "INSERT INTO reg  VALUES ('" + name + "','" + address + "','" + mobileno + "','" + emailid + "','"+house_no+"','"+ward_no+"','"+garbage_qty+"','"+balance+"')"
            mycursor.execute(sql)
            myconnection.commit()
            print(mycursor.rowcount, "value inserted.")
                #break
        elif choice=='A':
            print("write logic for admin login")
            print("select options ")
            print("1. for delete user by username")
            print("2. update information")
            print("3.View the detail")
            print("4........")
            ainput= int(input("please enter any choice : "))
                #Delete the row

            if ainput==1:
                namevar= input("enter the name  to delete: ")
                sql = "DELETE FROM reg WHERE name ='"+namevar+"'"
                mycursor.execute(sql,namevar)
                myconnection.commit()
                print("deleted row successfully")

                # Update the table
            elif ainput==2:
                nameold = input("enter the name to update")
                namenew = input('Enter Name:')
                address = input('Enter addd :')
                mobileno = input('Enter password:')
                emailid = input('Enter Email-Id:')
                garbage_qty = int(input("enter your garbadge qty : "))
                sql = "UPDATE reg SET name='" + namenew + "',address='" + address + "',mobileno='" + mobileno + "',emailid='" + emailid +"',garbageqty='"+garbage_qty+"', WHERE name= '"+nameold+"'"
                mycursor.execute(sql)
                myconnection.commit()
                print(mycursor.rowcount, "value updated.")
                #views the details
            elif ainput==3:
                print("under working .......")
                n=input("enter name to show detail")
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


except Error as e:
    print(e)
    print("some error occur")
finally:
    if myconnection.is_connected():
        mycursor.close()
        myconnection.close()
        print("MySQL connection is closed")



####################################################BACKUP####@@@@@@@@@@@222222222SS#################BBBBBBBBBBBB
# import mysql.connector
# print("Please enter any choice 1. L FOR LOGIN 2.R FOR  REGISTER")
# choice = input("enter your choice = ")
#
# try:
#     myconnection = mysql.connector.connect(host="localhost", user="root", password="root", database="db")
#     mycursor = myconnection.cursor()
#     if myconnection.is_connected():
#         print("connection is sucessful")
#         while choice == 'L' or choice == 'R':
#             if choice == 'L':
#                 name = input('Enter Name:')
#                 # addressvar = input("enter address")
#                 sql = "select name from reg"
#                 mycursor.execute(sql)
#                 record = mycursor.fetchall()
#
#                 i = 0
#                 while i < len(record):
#                     if name in record[i]:
#                         print("connected..,,,,")
#
#
#
#
#
#
#                         break
#                     i = i + 1
#
#                 break
#             else:
#                 print("Write logic for Register ")
#
#                 name = input('Enter Name:')
#                 address = input('Enter addd :')
#                 mobileno = input('Enter password:')
#                 emailid = input('Enter Email-Id:')
#
#                 sql = "INSERT INTO reg  VALUES ('" + name + "','" + address + "','" + mobileno + "','" + emailid + "')"
#                 mycursor.execute(sql)
#                 myconnection.commit()
#                 print(mycursor.rowcount, "value inserted.")
#                 break
#         else:
#             print("please enter a valid choice L for login R for register")
#     else:
#         print("connection is not connected")
#         mycursor = myconnection.cursor()
#
#
#
#
#
#
# except:
#     print("some error occur")
#
# finally:
#     if myconnection.is_connected():
#         mycursor.close()
#         myconnection.close()
#         print("MySQL connection is closed")






# #################################################BACKUP#################BBBBBBBBBBBB
# import mysql.connector
#
# print("Please enter any choice 1. L FOR LOGIN 2.R FOR  REGISTER")
# choice = input("enter your choice = ")
#
#
#
#
# myconnection = mysql.connector.connect(host="localhost", user="root", password="root", database="db")
# mycursor = myconnection.cursor()
# if myconnection.is_connected():
#     print("connection is sucessful")
# else:
#     print("connection is not connected")
#     mycursor = myconnection.cursor()
# if choice == 'L':
#     print("write logic for login")
#
#
#     name = input('Enter Name:')
#     # addressvar = input("enter address")
#     sql = "select name from reg"
#     mycursor.execute(sql)
#     record = mycursor.fetchall()
#
#     i = 0
#     while i < len(record):
#         if name in record[i]:
#             print("connected..,,,,")
#             break
#         i = i + 1
# elif choice=='R':
#     print("Write logic for Register ")
#
#     name = input('Enter Name:')
#     address = input('Enter addd :')
#     mobileno = input('Enter password:')
#     emailid = input('Enter Email-Id:')
#
#     sql = "INSERT INTO reg  VALUES ('" + name + "','" + address + "','" + mobileno + "','" + emailid + "')"
#     mycursor.execute(sql)
#     myconnection.commit()
#     print(mycursor.rowcount, "value inserted.")
# else:
#     print("please enter a valid choice L for login R for register")
# if myconnection.is_connected():
#     mycursor.close()
#     myconnection.close()
#     print("MySQL connection is closed")


#



