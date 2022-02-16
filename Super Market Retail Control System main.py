import mysql.connector as ms
from tabulate import tabulate
import os
from time import sleep
import csv
clear = lambda: os.system('cls')
def setup1():
    a1=input("Enter Host name:")
    a2=input("Enter user name:")
    a3=input("Enter Password:")
    data=[a1,a2,a3]
    file=open("Data.csv","w")
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()
    mycon=ms.connect(host=a1,user=a2,passwd=a3,database="mysql")
    if mycon.is_connected()==True:
        print("Connection Established")
        mycur=mycon.cursor()
    sleep(1)
    clear()
    print("Installing required items...Please Wait")   
    mycur.execute("create database supermarketretail")
    mycur.execute("use supermarketretail")
    mycur.execute("create table stock(itemcode int primary key not null,itemname varchar(30) not null,qty int,price float(15,2),discount float(15,2),dealername varchar(30))")
    mycur.execute("create table salerecord(customername varchar(30) ,phoneno bigint,amtpay float(15,2))")
    os.system("pip install pyinstaller")
    os.system("pip install tabulate")
    print("Initial Setup Done")
    input("Press Enter to Continue")
    mycon.commit()
    clear() 
def displaystockreco():
       try:
              query=("select * from stock")
              mycur.execute(query)
              mydata=mycur.fetchall()
              table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DEALER"]]
              for rec in mydata:
                     table.append(list(rec))
              print(tabulate(table))
       except:
              print("Invalid Choice")
       input("Press Enter To Continue")
       clear()        
def addstockreco():
       try:
              itemcode=int(input("Enter Item Code:"))
              itemname=input("Enter Item Name:")
              qty=int(input("Enter Quantity in Stock:"))
              price=float(input("Enter Price of Item:"))
              discount=int(input("Enter Discount % Applicable:"))
              dealer=input("Enter Name of Dealer:")
              query="insert into stock values({},'{}',{},{},{},'{}')".format(itemcode,itemname,qty,price,discount,dealer)
              mycur.execute(query)
              print("Record Succesfully Inserted")
              mycon.commit()
       except:
              print("Invalid Choice")
       input("Press Enter To Continue")
       clear()
def delstockreco():
       try:
              itemdel=int(input("Enter Item Code to be Deleted"))
              query="select * from stock where itemcode="+str(itemdel)
              mycur.execute(query)
              mydata=mycur.fetchone()
              deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DEALER"]]
              if mydata!=None:
                     deltable.append(list(mydata))
                     print(tabulate(deltable))
                     ans=input("Do you want to Delete?:")
                     if ans=="y" or ans=="Y":
                            query="delete from stock where itemcode="+str(itemdel)
              mycur.execute(query)
              mycon.commit()
       except:
              print("Invalid Choice")
       input("Press Enter To Continue")
       clear()
def searchstockreco():
       try:
              n=(input("Enter Item Name For Searching:"))
              query="select * from stock where itemname= '%s'" %(n)
              mycur.execute(query)
              mydata=mycur.fetchone()
              deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DEALER"]]
              if mydata!=None:
                     deltable.append(list(mydata))
                     print("Record Found And Is Available")
                     print(tabulate(deltable))
              mycur.execute(query)
              mycon.commit()
       except:
              if mydata==None:
                     print("Record Not Available")
       input("Press Enter To Continue")
       clear()
def modifystockreco():
       try:
              query=("select * from stock")
              mycur.execute(query)
              mydata=mycur.fetchall()
              table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DEALER"]]
              for rec in mydata:
                     table.append(list(rec))
              print(tabulate(table))
              modtable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DEALER"]]
              s=int(input("Enter Item Code For Modifying:"))
              query="select * from stock where itemcode="+str(s)
              mycur.execute(query)
              mydata=mycur.fetchone()
              if mydata!=None:
                     print("What Do you Want to Modify?")
                     print("1.Item Name")
                     print("2.Quantity")
                     print("3.Price")
                     print("4.Discount")
                     print("5.Dealer Name")
                     ch=int(input("Enter Your Choice"))
                     if ch==1:
                            i1=input("Enter New Item Name:")
                            query="update stock set itemname='{}' where itemcode={}".format(i1,s)
                     elif ch==2:
                            i2=int(input("Enter New Quantity:"))
                            query="update stock set qty={} where itemcode={}".format(i2,s)
                     elif ch==3:
                            i3=int(input("Enter New Price:"))
                            query="update stock set price={} where itemcode={}".format(i3,s)
                     elif ch==4:
                            i4=int(input("Enter New Discount:"))
                            query="update stock set itemname={} where itemcode={}".format(i4,s)
                     elif ch==5:
                            i5=input("Enter New Dealer Name:")
                            query="update stock set dealername='{}' where itemcode={}".format(i5,s)
              mycur.execute(query)
              print("Record Modified")
              query="select * from stock where itemcode="+str(s)
              mycur.execute(query)
              mydata=mycur.fetchone()
              modtable.append(list(mydata))
              print(tabulate(modtable))
              mycon.commit()  
       except:
              if mydata==None:
                     print("Record Not Available")
       input("Press Enter To Continue")
       clear()  
def dispbuyreco():
       query="select itemcode,itemname,qty,price,discount from stock"
       mycur.execute(query)
       table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
       mydata=mycur.fetchall()
       for rec in mydata:
              table.append(rec)
       print(tabulate(table))
       input("Press Enter To Continue")
def buyreco():
       global dtot
       dtot=0
       try:
              tot=0
              p1=int(input("Enter itemcode you want to buy:"))
              p2=int(input("Enter number you want to buy:"))
              mycur.execute("use supermarketretail")
              query=("select stock.price,stock.discount,stock.qty,salerecord.amtpay from stock,salerecord where stock.itemcode={} and salerecord.customername='{}'").format(p1,i1)
              mycur.execute(query)
              data=mycur.fetchone()
              mycon.commit()
              a,b,c,dtot=data
              if dtot==None:
                     dtot=0
              if c>=p2:
                     if c!=0:
                            d=c-p2
                            tot=tot+(p2*(a))
                            dtot+=tot*((100-b)/100)
                            query=("update salerecord set amtpay={} where customername='{}'").format(dtot,i1)
                            mycur.execute(query)
                            mycon.commit()
                            query=("update stock set qty={} where itemcode={}").format(d,p1)
                            mycur.execute(query)
                            mycon.commit()
                            input("ADDED TO CART,Press to continue")
                     else:
                            print("OUT OF STOCK")
                            input("Press Enter to continue")
                            clear()
                            menu1()
              else:
                     print("QTY Entered exceeds stock amount")
                     input("Press enter to continue")
       except:
              input("Please use valid choice")
              clear()
       clear()
def viewbill():
       query=("select customername,amtpay from salerecord where customername='{}'").format(i1)
       mycur.execute(query)
       data=mycur.fetchone()
       print("======BILL======")
       table=[["NAME","AMOUNT PAYABALE"]]
       table.append(list(data))
       print(tabulate(table))
       input("Press enter to continue")
       clear()
def adddetail():
       global i1
       i1=input("Enter Customer Name:")
       i2=int(input("Enter customer phone number:"))
       query="insert into salerecord(customername,phoneno) values('{}',{})".format(i1,i2)
       mycur.execute(query)
       mycon.commit()
       input("Press Enter To Continue")
       clear()
def dispsale():
    try:
              query=("select * from salerecord")
              mycur.execute(query)
              mydata=mycur.fetchall()
              table=[["NAME","PHONE NO.","AMOUNT RECIEVED"]]
              for rec in mydata:
                     table.append(list(rec))
              print(tabulate(table))
    except:
        print("Invalid Input")
    input("Press Enter To Continue")
    clear()        
def menu1():
       while True:
              print("=========MENU=========")
              tab=[["==Select Your Choice=="],["1.VIEW INVENTORY AND BUY"],["2.View Bill"],["3.Exit"]]
              print(tabulate(tab))
              ch=int(input("Enter Your Choice:"))
              if ch==1:
                     clear()
                     dispbuyreco()
                     buyreco()
              elif ch==2:
                     clear()
                     viewbill()
              elif ch==3:
                     clear()
                     break
              else:
                     print("Invalid choice")
                     clear()
def menu2():
       while True:
              print("=========MENU=========")
              tab=[["==Select Your Choice=="],["1.Display Stock Record"],["2.Add Stock Record"],["3.Modify Stock Record"],["4.Delete Stock Record"],["5.Search Stock Record"],["6.Display All Sales"],["7.Exit"]]
              print(tabulate(tab))
              ch=int(input("Enter Your Choice:"))
              if ch==1:
                     clear()
                     displaystockreco()
              elif ch==2:
                     clear()
                     addstockreco()
              elif ch==3:
                     clear()
                     modifystockreco()
              elif ch==4:
                     clear()
                     delstockreco()
              elif ch==5:
                     clear()
                     searchstockreco()
              elif ch==6:
                     clear()
                     dispsale()
              elif ch==7:
                  clear()
                  break
              else:
                     print("Invalid Choice")
                     clear()      
while True:
    print("=========MENU=========")
    tab=[["==Select Your Choice=="],["1.Initial Setup"],["2.Customer Mode"],["3.Employee Mode"],["4.Exit"]]
    print(tabulate(tab))
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        setup1()
    file=open("Data.csv")
    reader=csv.reader(file)
    try:
        for rec in reader:
            a1=rec[0]
            a2=rec[1]
            a3=rec[2]
            mycon=ms.connect(host=a1,user=a2,passwd=a3,database="mysql")
            if mycon.is_connected()==True:
                mycur=mycon.cursor()
                mycur.execute("use supermarketretail")
                mycon.commit()
    except:
        pass
        if ch==2:
            adddetail()
            clear()
            menu1()
            clear()
        elif ch==3:
            clear()
            menu2()
            clear()
        elif ch==4:
            clear()
            break
        else:
            print("Invalid Choice")
            clear()
    
