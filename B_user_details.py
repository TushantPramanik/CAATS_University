##--------------------------Personal Details----------------------------##

from itertools import count
from D_work_dep import skill, master
from C_school_dep import cls_9, cls_10, cls_11, cls_12
from E_clg_brch_choos import clg_brch

def per_det():

    for i in count():
        print("\n"+"="*30)
        print("PERSONAL DETAILS")
        print("="*30)


        print("\nProfession: 1. Student")
        print("            2. Work (your age must be above 17 !!! )")
        print("            3. Others")

        pro=int(input("\nChoose your option: "))

        if pro in (1,2,3):
             
            print("\n\nAge: 1. Lesser than 13")
            print("     2. 13-14")
            print("     3. 14-15")
            print("     4. 15-16")
            print("     5. 16-17")
            print("     6. 17+")

            age=int(input("\nChoose your option: "))
            
            if age in (1,2,3,4,5,6):
                
                if pro==1:
                    if age==1:
                        skill()
                        return
                    elif age==2:
                        print("\nSuggestions: 1. CLASS-9")
                        print("             2. SKILLS")

                        o_9=int(input("\nChoose your option: "))

                        if o_9==1:
                            cls_9()
                            return
                        elif o_9==2:
                            skill() 
                            return 
                        else:
                            print("\nWrong input. Try again!!!!......")


                    elif age==3:
                        print("\nSuggestions: 1. CLASS-10")
                        print("             2. SKILLS")

                        o_10=int(input("\nChoose your option: "))

                        if o_10==1:
                            cls_10()
                            return
                        elif o_10==2:
                            skill()
                            return
    
                        else:
                            print("\nWrong input. Try again!!!!......")



                    elif age==4:
                        print("\nSuggestions: 1. CLASS-11")
                        print("             2. SKILLS")

                        o_11=int(input("\nChoose your option: "))

                        if o_11==1:
                            cls_11()
                            return
                        elif o_11==2:
                            skill()
                            return
                        else:
                            print("\nWrong input. Try again!!!!......")

                    elif age==5:
                        print("\nSuggestions: 1. CLASS-12")
                        print("             2. SKILLS")


                        o_12=int(input("\nChoose your option: "))

                        if o_12==1:
                            cls_12()
                            return
                        elif o_12==2:
                            skill()
                            return 
                        else:
                            print("\nWrong input. Try again!!!!......")

                    elif age==6:
                        print("\nSuggestions: 1. COLLEGE")    
                        print("             2. SKILLS")

                        clg=int(input("\nChoose your option: "))

                        if clg==1:
                           #---- print("function of college")----#
                           clg_brch()
                           return
                        elif clg==2:
                            skill()
                            return
                        else:
                            print("\nWrong input. Try again!!!!......")
    
                
                elif pro==2 and age==6:
                    print("\nSuggestion: 1. SKILLS")
                    print("            2. MASTER CLASS (4 hours)")

                    o_wk=int(input("\nChoose your option: "))

                    if o_wk==1:
                        skill()
                        return
                    elif o_wk==2:
                        master()
                        return
                    else:
                        print("\nWrong input. Try again!!!!......")

                elif pro==3:
                    skill()
                    return
                else:
                    print("\nWrong input. Try again!!!!......")
            else:
                print("\nWrong input. Try again!!!!......")
        else:
            print("\nWrong input. Try again!!!!......")
    

    