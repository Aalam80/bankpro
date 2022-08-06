
import database as db

while True:
    print('''Select the operation to be performed:
    1. OPEN ACCOUNT
    2. DEOPSIT AMOUNT
    3. WITHDRAW BALANCE
    4. BALANCE ENQUIRY
    5. DISPLAY COUSTOMETR DETAILS
    6. UPDATE RECORDS
    7. CLOSE AN ACCOUNT
    0. EXIT
    ''')
    

    choice = int (input('Enter Your Choice:'))
    if choice==0:
        break
    elif choice==1:
        
        db.OpenAcc()
        
    elif choice==2:
        db.depoAmo()

        
    elif choice==3:
        db.witham()
        

    elif choice==4:
        db. balance()
    
    
    elif choice==5:


        db.dispacc()

    elif choice==6:
        db.update()   
     
    elif choice==7:
        db.closeac()
    
    
    
    
    else:
        print('wrong choice....')
        
    