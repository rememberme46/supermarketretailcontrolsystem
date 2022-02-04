import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",passwd="nps@123",database="supermarketretail")
if mycon.is_connected()==True:
       print("Connection Established")
       mycur=mycon.cursor()

def displaystockreco():
       query=("select * from stock")
       mycur.execute(query)
       mydata=mycur.fetchall()
       table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
       for rec in mydata:
              table.append(list(rec))
       print(tabulate(table))
              
def addstockreco():
       itemcode=int(input("Enter Item Code:"))
       itemname=input("Enter Item Name:")
       qty=int(input("Enter Quantity in Stock:"))
       price=float(input("Enter Price of Item:"))
       discount=int(input("Enter Discount % Applicable:"))
       query="insert into stock values({},'{}',{},{},{})".format(itemcode,itemname,qty,price,discount)
       mycur.execute(query)
       print("Record Succesfully Inserted")
       mycon.commit()
def delstockreco():
       itemdel=int(input("Enter Item Code to be Deleted"))
       query="select * from stock where itemcode="+str(itemdel)
       mycur.execute(query)
       mydata=mycur.fetchone()
       deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
       if mydata!=None:
              deltable.append(list(mydata))
              print(tabulate(deltable))
              ans=input("Do you want to Delete?:")
              if ans=="y" or ans=="Y":
                     query="delete from stock where itemcode="+str(itemdel)
       mycur.execute(query)
       mycon.commit()
def searchstockreco():
       try:
              s=(input("Enter Item Name For Searching:"))
              query="select * from stock where itemname="+str(s)
              mycur.execute(query)
              mydata=mycur.fetchone()
              deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
              if mydata!=None:
                     deltable.append(list(mydata))
                     print("Record Found And Is Available")
                     print(tabulate(deltable))
              mycur.execute(query)
              mycon.commit()
       except:
              if mydata==None:
                     print("Record Not Available")

def modifystockreco():
       try:
              query=("select * from stock")
              mycur.execute(query)
              mydata=mycur.fetchall()
              table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
              for rec in mydata:
                     table.append(list(rec))
              print(tabulate(table))
              modtable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT"]]
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

while True:
       print("=====MENU=====")
       ch=int(input("Enter User Mode(1.CUSTOMER/2.EMPLOYEE)-"))
       if ch==2:
              ch=int(input("Enter Table to Operate on(1.stock/2.transaction/3.payoutrecord/4.supplier)-"))
              if ch==1:
                     while True:
                            print("Select Your Choice")
                            print("1.Display Stock Record")
                            print("2.Add Stock Record")
                            print("3.Modify Stock Record")
                            print("4.Delete Stock Record")
                            print("5.Search Stock Record")
                            print("6.Exit")
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
                     else:
                            print("Invalid Choice")
              else:
                     print("Invalid Choice")
       
                            

       

