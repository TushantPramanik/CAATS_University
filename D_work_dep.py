##------------------------Work Department-------------------------------##
from itertools import count
from L_bat_prch import sk_prch, mas_prch

def master():
    for i in count():
        print("\n"+"~"*30)
        print("MASTER CLASS (4 hours)")
        print("~"*30)

        print("\nCourses: 1. AI and ML ")
        print("         2. Technical Leadership")
        print("         3. System Design")
        print("         4. Fundamentals of Cloud Computing")

        mast_cls=int(input("\nChoose your option: "))

        if mast_cls==1:
            print("\nintro of AI and ML \n")
            mas_prch()
            return
        elif mast_cls==2:
            print("\nintro of Technical Leadership \n") 
            mas_prch()
            return
        elif mast_cls==3:
            print("\nintro of System Design \n")  
            mas_prch()
            return 
        elif mast_cls==4:
            print("\nintro of Fundamentals of Cloud Computing \n")
            mas_prch()
            return 
        else:
            print("\nWrong input. Try again!!!!......")


def skill():
    for i in count():
        print("\n"+"~"*30)
        print("SKILLS TO UPGRADE YOURSELF")
        print("~"*30)

        print("\nSkills: 1.Content Creation")
        print("        2. Video Editing")
        print("        3. Digital Marketing")
        print("        4. Entrepreneurship")
        print("        5. Programming")
        print("        6. Graphic Designing")

        skl=int(input("\nChoose your option: "))

        if skl==1:
            print("\nJourney to the world of Content Creation\n ")
            sk_prch()
            return
        elif skl==2:
            print("\nJourney to the world of Video Editing \n ")
            sk_prch()
            return
        elif skl==3:
            print("\nJournry to the world of Digital Marketing \n")
            sk_prch()
            return
        elif skl==4:
            print("\nJourney to the world of Entrepreneurship \n ")
            sk_prch()
            return
        elif skl==5:
            print("\nJourney to the world of Programing \n")
            sk_prch()
            return
        elif skl==6:
            print("\nJournry to the world of Grafic Designing\n")
            sk_prch()
            return
        else:
            print("\nWrong input.Try again!!!!........")