from itertools import count
per_sem=None
sem=None
inn=None
duration = None


#================== B.Tech =================#

def btech_prch():
    global per_sem
    global sem
    global inn
    sem = 8
    per_sem = 80000
    print("~"*40)
    print(f"Per semester fees: {per_sem}")
    print(f"You have total semesters: {sem}")
    print(f"Your 4 years total fees: {per_sem*sem}\n")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Back to the previous menu")
        print("[EXIT]=> Exit from our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            from E_clg_brch_choos import clg_brch
            clg_brch()
            return

        elif inn == 'EXIT':
            print("Thank you for visiting our website")
            exit
            return

        else:
            print("\nWrong Input.. Try again...!!")

    

#=================== BCA ======================#

def bca_prch():
    global per_sem
    global sem
    per_sem= 50000
    sem=8
    print("~"*40)
    print(f"Per semester fees: {per_sem}")
    print(f"You have total semesters: {sem}")
    print(f"Your 4 years total fees: {per_sem*sem}\n")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Back to the previous menu")
        print("[EXIT]=> Exit from our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            from E_clg_brch_choos import clg_brch
            clg_brch()
            return
        
        elif inn == 'EXIT':
            print("Thank you for visiting our website")
            exit
            return
            
        else:
            print("\nWrong Input.. Try again...!!")

            


#=======================BSc.=====================#            
 
def bsc_prch():
    global per_sem
    global sem
    per_sem= 30000
    sem=8
    print("~"*40)
    print(f"Per semester fees: {per_sem}")
    print(f"You have total semesters: {sem}")
    print(f"Your 4 years total fees: {per_sem*sem}\n")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Back to the previous menu")
        print("[EXIT]=> Exit from our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            from E_clg_brch_choos import clg_brch
            clg_brch()
            return
        
        elif inn == 'EXIT':
            print("Thank you for visiting our website")
            exit
            return
            
        else:
            print("\nWrong Input.. Try again...!!")



            
#=======================DIPLOMA=====================#            
 
def dip_prch():
    global per_sem
    global sem
    per_sem= 25000
    sem=6
    print("~"*40)
    print(f"Per semester fees: {per_sem}")
    print(f"You have total semesters: {sem}")
    print(f"Your 3 years total fees: {per_sem*sem}\n")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Back to the previous menu")
        print("[EXIT]=> Exit from our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            from E_clg_brch_choos import clg_brch
            clg_brch()
            return

        elif inn == 'EXIT':
            print("Thank you for visiting our website")
            exit
            return
            
        else:
            print("\nWrong Input.. Try again...!!")
           





#================School===============#

def scl_brds_prch():
    global duration
    global inn
    per_sem = 5000
    duration = 12
    
    print("~" * 40)
    print(f"\nTotal course duration:- {duration} month")
    print(f"Per month fees:- {per_sem}")
    print (f"\nTotal course fees:-{per_sem * duration}")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Exit form our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            print("Thank you for visiting our website...")
            exit
            return
        else:
            print("\nWrong Input.. Try again...!!")
            

def scl_oly_prch():
    global duration
    global inn
    per_sem = 10000
    duration = 8
    
    print("~" * 40)
    print(f"\nTotal course duration:- {duration} month")
    print(f"Per month fees:- {per_sem}")
    print (f"\nTotal course fees:-{per_sem * duration}")
    
    for i in count():
        print("[YES]=> Purchase the Batch")
        print("[NO]=> Exit form our website")
        
        inn=str(input(("Enter your choice: "))).upper() 
        if inn == 'YES':
            print("*"*60)
            print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
            print("*"*60)
            return

        elif inn == 'NO':
            print("Thank you for visiting our website")
            exit
            return
        else:
            print("\nWrong Input.. Try again...!!")



#================== SKILLS ==================#

def sk_prch():
    global duration
    global per_sem
    per_sem = 3000
    print("\nPer Month coaching fees: 3000 \n")
    print("We provide courses for:[A] 3 Months")
    print("                      :[B] 6 Months")
    print("                      :[C] 9 Months")
    print("                      :[D] 12 Months")
    
    duration = str(input("\nEnter your duration:- ")).upper()
    
    for i in count():

        if duration == 'A':
            print(f"\nFor 3 months-- Your total fees: {per_sem*3}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()         

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                else:
                    print("\nWrong Input.. Try again...!!")

        elif duration == 'B':
            print(f"\nFor 6 months-- Your total fees: {per_sem*6}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                else:
                    print("\nWrong Input.. Try again...!!")
            
        elif duration == 'C':
            print(f"\nFor 9 months-- Your total fees: {per_sem*9}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                else:
                    print("\nWrong Input.. Try again...!!")

        elif duration == 'D':
            print(f"\nFor 12 months-- Your total fees: {per_sem*12}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                else:
                    print("\nWrong Input.. Try again...!!")
            
        else:
            print("\nWrong input..Try again..!!!")

#================Master Class===================#            

def mas_prch():

    global duration
    global per_sem
    per_sem = 500
    print("\nPer week coaching fees: 500 \n")
    print("We provide courses for:[A] 1 Week")
    print("                      :[B] 2 Weeks")
    print("                      :[C] 3 Weeks")
    print("                      :[D] 4 Weeks")
    
    duration = str(input("\nEnter your duration:- ")).upper()
    
    for i in count ():

        if duration == 'A':
            print(f"\nFor 1 Week-- Your total fees: {per_sem*1}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()         

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                    
                else:
                    print("\nWrong Input.. Try again...!!")

        elif duration == 'B':
            print(f"\nFor 2 Weeks -- Your total fees: {per_sem*2}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                    
                else:
                    print("\nWrong Input.. Try again...!!")
            
        elif duration == 'C':
            print(f"\nFor 3 weeks-- Your total fees: {per_sem*3}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                    
                else:
                    print("\nWrong Input.. Try again...!!")

        elif duration == 'D':
            print(f"\nFor 4 weeks-- Your total fees: {per_sem*4}\n")

            for i in count():
                print("[YES]=> Purchase the Batch")
                print("[NO]=> Back to the previous menu")
                print("[EXIT]=> exit from our website ")
                inn=str(input(("Enter your choice: "))).upper() 
                if inn == 'YES':
                    print("*"*60)
                    print("\n !!!___YOUR BATCH HAS BEEN PURCHASED SUCCESSFULLY___!!!\n")
                    print("*"*60)
                    return

                elif inn == 'NO':
                    from B_user_details import per_det
                    per_det()        

                elif inn == 'EXIT':
                    print("\nThank you for visiting our website")
                    exit
                    return
                    
                else:
                    print("\nWrong Input.. Try again...!!")
            
        else:
            print("\nWrong input..Try again..!!!")