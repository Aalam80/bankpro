import pymysql
import mysql.connector as a
from balancEroor import balancEroor
con=a.connect (host='localhost',
             database='bankm',
             user='root',
            password='')



def OpenAcc():

    
    n = input("Enter Name : ")
    ac = input("Enter Account No: ")
    db = input("Enter D.O.B: ")
    ad= input("Enter Address : ")
    p = input("Enter Phone : ")
    ob = int(input("Enter Opening Balance :"))
    if ob <5000:
        print('opening bal must be 5000 or more')
    else:    
        data1 = (n,ac,db,ad,p,ob)
        data2 = (n,ac,ob)
        sql1 = 'insert into account values(%s, %s,%s,%s,%s,%s)'
        sql2 = 'insert into amount values(%s,%s,%s)'
        c = con.cursor()
        c.execute(sql1,data1)
        c.execute(sql2,data2)
        con.commit()
        print("Data Entorod Successfully")
    
    
    

def depoAmo():
    
    am = int(input("Enter Amount: ")) 
    ac = input('Enter Account no')
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0] + am
    sql = "update amount set balance = %s where acno=%s"
    d = (tam,ac)
    c.execute(sql,d)
    con.commit()
    print('amount deposit Successfully')
    
    


def witham():
    
    try:
       am = int(input("Enter Amount: "))
       ac= input("Enter Account no:")
    
       a = "select balance from amount where acno = %s"
       data = (ac,)
       c = con.cursor()
       c.execute(a,data)
       myresult = c.fetchone()[0]
       #print(myresult)
    
       if myresult<=5000:
              raise balancEroor('insafficiant bal')
       else:
    
    
        tam = myresult - am
        sql = " update amount set balance = %s where acno = %s"
        d = (tam,ac)
        c.execute(sql,d)
        con.commit()
        print('amount withdraw Successfully')
    except balancEroor as e:
        print(e)
    


def balance():
    
    ac = input("Enter Account No: ")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance for Account : ",ac," is ",myresult[0]) 
    
    



def dispacc():   
    

    ac = input("Enter Account No: ")
    a = "select * from account where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchall()
    for i in myresult:
        #print(i)

         print(f'name: {i[0]}\naccount no: {i[1]}\nDOB: {i[2]}\nAddress: {i[3]}\nphone: {i[4]}\nopening bal: {i[5]}')



   


def update():
    acno=input('enter account no:')
    name=input('enter new owner name')
    query1="update account set name= '{}' where acno= {}".format(name,acno)
    query2="update amount set name= '{}' where acno= {}".format(name,acno)
    c = con.cursor()
    c.execute(query1)
    c.execute(query2)
    con.commit()
    print('Account updated Successfully ')


    


def closeac():

    ac =input("Enter Account No: ")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print('Account close Successfully ')

   
          

    
     





