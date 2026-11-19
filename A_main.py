##--------------------------Personal Details----------------------------##

from itertools import count
from D_work_dep import skill, master
from C_school_dep import cls_9, cls_10, cls_11, cls_12
from L_bat_prch import scl_brds_prch, scl_oly_prch, sk_prch, mas_prch

##----------------------------------login portal-------------------------------------##

uid = None
password = None

def register():
    print("\n")
    print("-"*30)
    print("Register")
    print("-"*30)
    print("\n")

    global uid
    global password
    print('Sample user id: "name@caats.edu" ')
    user = input("Enter your user id: ")
    if "@caats.edu" in user :
        while True:
            print("\n(Atleast four digit. Could be a combination of number, alphabet, symbols.)")
            print("Sample password: pass@12#in")
            passw1 = input("Set your strong password: ")

            if len(str(passw1)) >= 4:
                passw2 = input("Re-enter your password:-")
                if passw1 == passw2:
                    uid = user
                    password = passw2
                    print("\nAccount created successfuly....\n")
                    break

                else:
                    print("\nPlease enter the same password.\n")
            
            else:
                print("\nThe password is very weak !!!....\nEnter a strong password.\n")
            
            
    else:
        print("\nIncorrect format!\nEnter user id in a valid format.\n")
        register()


def login():
        print("\n")
        print("-"*30)
        print("Login")
        print("-"*30)
        print("\n")

        if uid == None and password == None :
            print("\nYou are not registered yet !!!\n")
            main()

        else:
            user = input("Enter your user id:-")
            
            if user == uid:
                passw2 = input("Enter your password:-")
                if password == passw2:
                    print("\nLogin successfuly.\n")                    
                    
                else:
                    print("\npassword is incorrect.\nLooks like you forgot your password.\n")
                    forget_password()
            else:
                print("\nWrong user id!\nPlease enter a correct user id.\n")
                login()
                


def forget_password():
    print("\n")
    print("-"*30)
    print("Forgot Password")
    print("-"*30)
    print("\n")

    global password
    if uid == None and password == None :
        print("\nYou are not registered yet !!!\n")
        main()
    
    else:
        user = input("Enter your user id:-")
            
        if user == uid:
            passw2 = input("Enter your password:-")
            password = passw2
            print("\nPassword changed successfuly.\n")

        else:
            print("\nWrong user id!\nPlease enter a correct user id.\n")
            forget_password()


    ## ---- main---- ##
def main():
    print("\n")
    print("="*30)
    print("Login Portal")
    print("="*30)

    print("1. Register\n2. Login\n3. forgot password")

    x = int(input("Enter your choice:-"))

    match x:
        case 1:
            register()
            main()
        case 2:
            login()
        case 3:
            forget_password()
            main()
        case _:
            print("\nWrong input !! Try again\n")
            main()

main()

from B_user_details import per_det
per_det()