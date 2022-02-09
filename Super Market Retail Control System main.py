import mysql.connector as ms
from tabulate import tabulate
import os
from time import sleep
clear = lambda: os.system('cls')



mycon=ms.connect(host="localhost",user="root",passwd="nps@123",database="supermarketretail")
if mycon.is_connected()==True:
       print("Connection Established")
       mycur=mycon.cursor()
       sleep(1)
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
def buyreco():
       while True:
              p1=int(input("Enter Itemcode you want to buy:"))
              p2=int(input("Enter Number of items you want to buy:"))
              query="select discount from stock where itemcode="+str(p1)
              mycur.execute(query)
              mydata=mycur.fetchone()
              print(mydata,type(mydata))
def menu1():
       while True:
              print("=========MENU=========")
              tab=[["==Select Your Choice=="],["1.View Inventory"],["2.BUY"],["3.View Bill"],["4.Exit"]]
              print(tabulate(tab))
              ch=int(input("Enter Your Choice:"))
              i1=input("Enter Customer Name:")
              i2=int(input("Enter customer phone number:"))
              query="insert into salrecord values('{}',{})".format(i1,i2)
              if ch==1:
                     dispbuyreco()

              if ch==2:
                     buyreco()
                            
              
def menu2():
       
       while True:
              print("=========MENU=========")
              tab=[["==Select Your Choice=="],["1.Display Stock Record"],["2.Add Stock Record"],["3.Modify Stock Record"],["4.Delete Stock Record"],["5.Search Stock Record"],["6.Exit"]]
              print(tabulate(tab))
              ch=int(input("Enter Your Choice:"))
              if ch==1:
                     displaystockreco()
              elif ch==2:
                     addstockreco()
              elif ch==3:
                     modifystockreco()
              elif ch==4:
                     delstockreco()
              elif ch==5:
                     searchstockreco()
              elif ch==6:
                     break
              else:
                     print("Invalid Choice")

while True:
              print("=========MENU=========")
              tab=[["==Select Your Choice=="],["1.Customer Mode"],["2.Employee Mode"],["3.Exit"]]
              print(tabulate(tab))
              ch=int(input("Enter Your Choice:"))
              if ch==1:
                     menu1()
              elif ch==2:
                     menu2()
              elif ch==3:

                     break
              else:
                     print("Invalid Choice")
                            

       

