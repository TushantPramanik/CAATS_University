from itertools import count
from F_Btech_clg_dep import btech_main
from G_Bsc_clg_dep import bsc_main
from I_Bca_clg_dep import bca_main
from K_diploma_clg_dep import diploma_main

def clg_brch():
    for i in count():
        print("\n"+"~"*30)
        print("COLLEGE")
        print("~"*30)

        res_12=float(input("\nEnter your 12th percentage: "))

        if res_12>=75 and res_12<=100:
            print("\nBranches: 1. BTECH")
            print("          2. BSc.")
            print("          3. BCA")
            print("          4. Diploma")

            brch_up=int(input("\nChoose your option: "))

            if brch_up==1:
                btech_main()
                return
            elif brch_up==2:
                bsc_main(res_12)
                return
            elif brch_up==3:
                bca_main(res_12)
                return
            elif brch_up==4:
                diploma_main(res_12)
                return
            else:
                print("\nWrong input. Try again!!!!......")

        elif res_12>=55 and res_12<75:
            print("\nBranches: 1. BSc")
            print("          2. BCA")
            print("          3. Diploma")

            brch_down=int(input("\nChoose your option: "))

            if brch_down==1:
                bsc_main(res_12)
                return
            elif brch_down==2:
                bca_main(res_12)
                return
            elif brch_down==3:
                diploma_main(res_12)
                return
            else:
                print("\nWrong input. Try again!!!!......")

        elif res_12>=40 and res_12<55:
            print("\nBranches: 1. BSc")
            print("           2. Diploma")

            brch_down=int(input("\nChoose your option: "))

            if brch_down==1:
                bsc_main(res_12)
                return
            elif brch_down==2:
                diploma_main(res_12)
                return
            else:
                print("\nWrong input. Try again!!!!......")

        elif res_12>=33 and res_12<40:
            print("\nBranches: 1. Diploma")
            brch_down=int(input("\nChoose your option: "))

            if brch_down==1:
                diploma_main(res_12)
                return
            else:
                print("\nWrong input. Try again!!!!......")
        
        elif res_12<33 and res_12>=0:
            print("\nYou failed in class 12.\nSorry admission is not possible!!!!!!")
            return

        else:
            print("\nInvalid input. Try again:(!!!!......")