from L_bat_prch import bca_prch

def bca_main(res_12):
    print("  ","="*35,"  ")
    print("||          CAATS UNIVERSITY          ||")
    print("||       BCA COUNSELLING PORTAL       ||")
    print("  ","="*35,"  ")

    print("\nCongratulation on choosing BCA")

    print("""\nYou Are Interested in BCA — 
    Expert Counselling Now Available Based on Your 
    Academic Marks and Career Interests.""")
    

    while True:
        print("\n","-"*30)
        print("BCA Branch Selection.")
        print("-"*30,"\n")
        print("\n:::The Required Parameters:::  ")
        print(f"Your class 12 percentage: {res_12}%")

        if res_12 >= 80 and res_12 <=100:
            print("""Our recomendation for your BCA branch is---
    1. Artificial Intelligence and Machine Learning.
    2. Cloud Computing.
    3. Cyber Security.
    4. Software Devlopment.
    5. Internet of Things.
    """)
            choice =int(input("\nEnter your choice for your BCA branch:-"))

            if choice == 1:
                print("\nWelcome to Artifical Intelligence.")
                bca_prch()
                break
            elif choice == 2:
                print("\nWelcome to Cloud Computing.")
                bca_prch()
                break
            elif choice == 3:
                print("\nWelcome to Cyber Security.")
                bca_prch()
                break
            elif choice == 4:
                print("\nWelcome to Software Devlopment.")
                bca_prch()
                break
            elif choice == 5:
                print("\nWelcome to Internet of Things.")
                bca_prch()
                break
            else:
                print("\ninvalid option! Please try again....!!!!!!")


        elif res_12 >= 75 and res_12<80:
            print("""Our recomendation for your BCA branch is---
    1. Cloud Computing.
    2. Cyber Security.
    3. Software Devlopment.
    4.Internet of Things.
    """)
            choice =int(input("\nEnter your choice for your BCA branch:-"))

            if choice == 1:
                print("\nWelcome to Cloud Computing.")
                bca_prch()
                break
            elif choice == 2:
                print("\nWelcome to Cyber Security.")
                bca_prch()
                break
            elif choice == 3:
                print("\nWelcome to Software Devlopment.")
                bca_prch()
                break
            elif choice == 4:
                print("\nWelcome to Internet of Things.")
                bca_prch()
                break
            else:
                print("\ninvalid option! Please try again....!!!!!!")
         

        elif res_12 >= 65 and res_12<70:
            print("""Our recomendation for your BCA branch is---
    1. Cyber Security.
    2. Software Devlopment.
    3. Internet of Things.
    """)
            choice =int(input("\nEnter your choice for your BCA branch:-"))

            if choice == 1:
                print("\nWelcome to Cyber Security.")
                bca_prch()
                break
            elif choice == 2:
                print("\nWelcome to Software Devlopment.")
                bca_prch()
                break
            elif choice == 3:
                print("\nWelcome to Internet of Things.")
                bca_prch()
                break
            else:
                print("\ninvalid option! Please try again....!!!!!!")


        elif res_12 >= 60 and res_12<65:
            print("""Our recomendation for your BCA branch is---
    1. Software Devlopment.
    2. Internet of Things.
    """)
            choice =int(input("Enter your choice for your BCA branch:-"))

            if choice == 1:
                print("\nWelcome to Software Devlopment.")
                bca_prch()
                break
            elif choice == 2:
                print("\nWelcome to Internet of Things.")
                bca_prch()
                break
            else:
                print("\ninvalid option! Please try again....!!!!!!")


        elif res_12 >= 55 and res_12<60:
            print("You have only one branch based on your marks\nInternet of Things.")
            choice = input("Do you want to select this branch YES or NO:-")
            
            if choice == "yes" or choice == "YES" or choice == "Yes":
                print("\nwelcome to Internet of Things.")
                bca_prch()
                break
            elif choice == "no" or choice == "NO" or choice == "No":
                print("\nThank you for using our system.")
                bca_prch()
                break
            else:
                print("\ninvalid option! Please try again....!!!!!!")


        elif res_12<55 and res_12>=0:
            print("""\n!!!You are not eligible for BCA!!!
            ----Try something else----""")
            break


        else:
            print("Invalid input ! Please try again.........!!!!!")
            continue