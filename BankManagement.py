import mysql.connector
import sys


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="bank")

cursor=mydb.cursor()
mydb.commit()
cursor.execute("create database if not exists bank")
cursor.execute("create table if not exists accounts(username varchar(50), name varchar(50), address varchar(50), balance int not null, password varchar(20))")

#cursor.execute("Insert into accounts (username, name, address, balance, password) values ("Ajith Kumar", "Ajith", "TamilNadu", 1000, "Alien@1234"), ("Akish krishnan", "Akish", "Senthi Nagar", 500, "Akish@1234")")

name = input("Enter your name: ")
password = input("Enter your password: ")
value = (name, password)
cursor.execute("Select name, password from accounts where name=%s and password=%s", value)

for i in cursor:
    global nam
    global passwd
    nam, passwd = i
    
if(name == nam and password == passwd):
    print("\nSuccessfully Login\n")
    while(True):
        print("1. Display Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Exit")
        print("\nEnter the choice :")
        choice = int(input(">>> "))

        if choice == 1:
            cursor.execute("Select * from accounts where name=%s and password=%s", value)

            for i in cursor:
                Username, name, address, balance, password = i
                print(f"Username : {Username}")
                print(f"Name : {name}")
                print(f"Address : {address}")
                print(f"Balance : {balance}")

        elif choice == 2:
            amount = int(input("Enter deposit Amount : "))
            cursor.execute("select balance from accounts where name=%s and password=%s", value)

            for i in cursor:
                balance = i[0]

                total = amount + balance
                u=value[0]
                p=value[1]
                val=(total,u,p)
                print(val)
                cursor.execute("update accounts set balance=%s where name=%s and password=%s", val)
                mydb.commit()

        elif choice == 3:
            wdraw = int(input("Enter withdraw money amount : "))

            cursor.execute("select balance from accounts where name=%s and password=%s", value)

            for i in cursor:
                balance = i[0]

                if balance >= wdraw:
                    total = balance - wdraw
                    u=value[0]
                    p=value[1]
                    val=(total,u,p)
                    print("Successfully Withdraw")
                    cursor.execute("update accounts set balance=%s where name=%s and password=%s", val)
                    print(f"Remaining Balance : {total}")
                else:
                    print("Insufficient Balance")

        elif choice == 4:
            receiver = input("Enter the receiver name: ")
            money = int(input("Enter how much money transfer :"))
            cursor.execute("Select name, balance from accounts where name=%s",(receiver,)) # receiver 
            for i in cursor:
                rec, balance = i

                cursor.execute("select balance from accounts where name=%s and password=%s", value)  # current user

                for i in cursor:
                    bal = i[0]

                    
                if receiver == rec:
                    if bal >= money:
                        transfer_money = balance + money

                        cursor.execute("update accounts set balance=%s where name=%s", (transfer_money, rec))

                        remaining_balance = bal - money
                        u=value[0]
                        p=value[1]
                        val=(remaining_balance,u,p)
                        cursor.execute("update accounts set balance=%s where name=%s and password=%s", val)
                        print("transfered Successfully")

                        print(f"Remaining Balance: {remaining_balance}")
                        break
                    else:
                        print("Insufficient Balance")
                        break
            else:
                print("Receiver Not Available")


        elif choice == 5:
            sys.exit(0)
                    

else:
    print("Invalid Account")

