##--------------------------Collage Department---------------------------------##

## ============= B.TECH ============== ##
from itertools import count
from L_bat_prch import btech_prch
c_jee = None
inter = None
ch = None


def btech_main():

    global inter
    global c_jee
    global ch
    for i in count():
        print("  ","="*33,"  ")
        print("||        CAATS UNIVERSITY         ||")
        print("||    B.TECH COUNSELLING PORTAL    ||")
        print("  ","="*33,"  ")

        print("\nCongratulations on choosing B.Tech")

        print("""\nThe system will now guide you in selecting the most
    appropriate branch and specialization based on your
    academic performance and interests.""")

        print("\n:::Parameters Considered:::")
        c_jee = float(input("-> CAATS JEE Percentile: "))


        # ========================== BLOCK 1: JEE >= 85 ==========================
        if c_jee>=85 and c_jee<=100:

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""   
        1. Programming
        2. Artificial Intelligence
        3. Security & Hacking
        4. Data Analysis
        5. Electronics
        6. Machines & Automobiles 
        7. Construction & Design
        8. Electrical Systems""")
            
            inter = int (input("\nEnter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CORE CSE")
                print("2. CSE AI/ML")
                print("3. CSE Data Science")
                print("4. CSE Cyber Security")
                print("5. INFORMATION TECHNOLOGY")
                print("6. CSE IOT")

                ch=int(input("\nEnter your choice: ")) 

                if ch==1:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the CSE AI/ML_________!!") 
                    btech_prch() 
                    break
                elif ch==3:
                    print("\n!!_______Journey to the CSE DS_________!!")
                    btech_prch()  
                    break
                elif ch==4:
                    print("\n!!_______Journey to the CSE CYBER_________!!") 
                    btech_prch()  
                    break  
                elif ch==5:
                    print("\n!!_______Journey to the IT_________!!")
                    btech_prch()  
                    break
                elif ch==6:
                    print("\n!!_______Journey to the CSE IOT_________!!") 
                    btech_prch()  
                    break         
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")            

            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CORE CSE")
                print("2. CSE (AI & ML)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the CSE (AI & ML)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CORE CSE")
                print("2. CSE Cyber Security")
                print("3. Information Security")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the CSE Cyber Security_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the Information Security_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 4:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CSE Data Science")
                print("2. Big Data Analytics")
                print("3. CORE CSE")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CSE Data Science_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Big Data Analytics_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 5:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electronics & Communication Engineering (ECE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electronics & Communication Engineering (ECE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter== 6:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Mechanical Engineering")
                print("2. Automobile Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Mechanical Engineering_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Automobile Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 7:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Civil Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Civil Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 8:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electrical Engineering (EE)")
                print("2. Electrical & Electronics Engineering (EEE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electrical Engineering (EE)_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Electrical & Electronics Engineering (EEE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")
            
            else:
                print("404 error..try again..!!")

        else:
            print("\nPercentile must be within '100'....!!!!\n")


        # ========================== BLOCK 2: JEE 75 - 84 ==========================
        if c_jee>=75 and c_jee<= 84 :

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""    
        1. Programming
        2. Security & Hacking
        3. Data Analysis
        4. Electronics
        5. Machines & Automobiles 
        6. Construction & Design
        7. Electrical Systems""")
            
            inter = int (input("\nEnter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")       
                print("1. CSE Data Science")
                print("2. CSE Cyber Security")
                print("3. INFORMATION TECHNOLOGY")
                print("4. CSE IOT")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CSE Data Science_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the CSE Cyber Security_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the INFORMATION TECHNOLOGY_________!!")
                    btech_prch()
                    break
                elif ch==4:
                    print("\n!!_______Journey to the CSE IOT_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")
            
            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CORE CSE")
                print("2. CSE Cyber Security")
                print("3. Information Security")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the CSE Cyber Security_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the Information Security_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")
            
            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CSE Data Science")
                print("2. Big Data Analytics")
                print("3. CORE CSE")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CSE Data Science_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Big Data Analytics_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 4:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electronics & Communication Engineering (ECE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electronics & Communication Engineering (ECE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 5:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Mechanical Engineering")
                print("2. Automobile Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Mechanical Engineering_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Automobile Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")
            
            elif inter == 6:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Civil Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Civil Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 7:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electrical Engineering (EE)")
                print("2. Electrical & Electronics Engineering (EEE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electrical Engineering (EE)_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Electrical & Electronics Engineering (EEE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            else:
                print("404 error ")
            

        # ========================== BLOCK 3: JEE 65 - 74 ==========================
        if c_jee>=65 and c_jee<= 74:

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""    
        1. Data Analysis
        2. Electronics
        3. Machines & Automobiles 
        4. Construction & Design
        5. Electrical Systems""")
            
            inter = int (input("\nEnter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. CSE Data Science")
                print("2. Big Data Analytics")
                print("3. CORE CSE")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the CSE Data Science_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Big Data Analytics_________!!")
                    btech_prch()
                    break
                elif ch==3:
                    print("\n!!_______Journey to the CORE CSE_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electronics & Communication Engineering (ECE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electronics & Communication Engineering (ECE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Mechanical Engineering")
                print("2. Automobile Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Mechanical Engineering_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Automobile Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")
            
            elif inter == 4:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Civil Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Civil Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 5:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electrical Engineering (EE)")
                print("2. Electrical & Electronics Engineering (EEE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electrical Engineering (EE)_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Electrical & Electronics Engineering (EEE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            else:
                print("404 error ")


        # ========================== BLOCK 4: JEE 55 - 64 ==========================
        if c_jee>=55 and c_jee<= 64:

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""    
        1. Electronics
        2. Machines & Automobiles 
        3. Construction & Design
        4. Electrical Systems\n""")
            
            inter = int (input("Enter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electronics & Communication Engineering (ECE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electronics & Communication Engineering (ECE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Mechanical Engineering")
                print("2. Automobile Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Mechanical Engineering_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Automobile Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Civil Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Civil Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 4:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electrical Engineering (EE)")
                print("2. Electrical & Electronics Engineering (EEE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electrical Engineering (EE)_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Electrical & Electronics Engineering (EEE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            else:
                print("404 error ")


        # ========================== BLOCK 5: JEE 45 - 54 ==========================
        if c_jee>=45 and c_jee<=54 :

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""    
        1. Machines & Automobiles 
        2. Construction & Design
        3. Electrical Systems
        4. Production
        5. Agricultural\n""")
            
            inter = int (input("Enter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Mechanical Engineering")
                print("2. Automobile Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Mechanical Engineering_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Automobile Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Civil Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Civil Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Electrical Engineering (EE)")
                print("2. Electrical & Electronics Engineering (EEE)")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Electrical Engineering (EE)_________!!")
                    btech_prch()
                    break
                elif ch==2:
                    print("\n!!_______Journey to the Electrical & Electronics Engineering (EEE)_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 4:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Production Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Production Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 5:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Agricultural Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Agricultural Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            else:
                print("404 error")


        # ========================== BLOCK 6: JEE 35 - 44 ==========================
        if c_jee>= 35 and c_jee<= 44:

            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""    
        1. Agricultural
        2. Food 
        3. Printing\n""")
            
            inter = int (input("Enter your choice--> "))

            if inter == 1:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Agricultural Engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Agricultural Engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 2:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Food technology")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Food technology_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            elif inter == 3:
                print("\n:: Based on your all criteria your recomended part is---\n")
                print("1. Printing engineering")

                ch=int(input("\nEnter your choice: "))
                if ch==1:
                    print("\n!!_______Journey to the Printing engineering_________!!")
                    btech_prch()
                    break
                else:
                    print("\nWRONG INPUT. TRY AGAIN.........!!!!!")

            else:
                print("404 error.Try again......!!!!!")