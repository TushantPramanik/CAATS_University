from itertools import count
from L_bat_prch import dip_prch
res_10 = None
inter = None

def diploma_main(res_12):
    global res_10
    global inter
    for i in count():
        print("\n"+"  ","="*35,"  ")
        print("||          CAATS UNIVERSITY          ||")
        print("||      DIPLOMA COUNSELLING PORTAL    ||")
        print("  ","="*35,"  ")

        print("\n!Congratulation on choosing DIPLOMA/POLYTECHNIC COURSE!")

        print("""\nYou Are Interested in DEPLOMA COURSE. — 
        Expert Counselling Now Available Based on Your 
        Academic Marks and Career Interests.""")
        
        print("\n:::The Required Parameters:::  ")
        print(f"\n-> 12th Percentage: {res_12}%")
        res_10 = float(input("-> 10th percentage: "))

        if res_12>=34 and res_12 <=100 and res_10>=35 and res_10<=100 :
            print( '''\nAccording to your score you are eligible for......
                1.Civil Engineering
                2.Mechanical Engineering 
                3.Electrical Engineering
                4.Electronics AND Communications
                5.Automobile Engineering ''')
            inter = int(input("\nEnter your choice:-"))
            if inter==1:
                print("\nYou have chosen Civil Engineering - shaping the future through roads, bridges, and modern infrastructure!!")
                dip_prch()
                break
            elif inter==2 :
                print("\nYou have chosen Mechanical Engineering - bringing machines and innovation to life..")
                dip_prch()
                break
            elif inter==3 :
                print("\nYou have chosen Electrical Engineering - powering the world with electricity and technology.")
                dip_prch()
                break
            elif inter==4 :
                print("\nYou have chosen Electronics & Communication Engineering - connecting people through advanced communication systems.")
                dip_prch()
                break
            elif inter==5 :
                print("\nYou have chosen Automobile Engineering - driving innovation in the automotive industry.")
                dip_prch()
                break
            else :
                print(" \n\n WRONG INPUT! PLEASE TRY AGAIN.......!!!!")

        elif res_12<34 and res_12>0 and res_10>0 and res_10<35:
            print("\nSorry you failed in your previous examination....!!!\nAdmission not possible ")
        else:
            print("\n\n\n !! WRONG INPUT. PLEASE ENTER YOUR MARKS PROPERLY !! ")