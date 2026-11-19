from itertools import count
from L_bat_prch import bsc_prch
inter = None

def bsc_main(res_12):
    global inter
    for i in count():
        print("  ","="*35,"  ")
        print("||          CAATS UNIVERSITY          ||")
        print("||       B.SC COUNSELLING PORTAL      ||")
        print("  ","="*35,"  ")

        print("\nCongratulation on choosing B.SC")

        print("""\nYou Are Interested in B.Sc. — 
        Expert Counselling Now Available Based on Your 
        Academic Marks and Career Interests.""")
        
        print("\n:::The Required Parameters:::  ")
        print(f"\n-> 12th Percentage: {res_12}%")

        if res_12>=75 and res_12<=100:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                1. B.SC in Physics:
                2. B.SC in Mathematics:
                3. B.SC in Statistic:
                4. B.SC in Economics:
                5. B.SC in Computer Science:
                6. B.SC in Chemisty:
                7. B.SC in Electronics:
                8. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choice:"))

            if inter==1:
                print("\n----Your jouney to the world of Physics---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Mathematics---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journey to the world of Statistics---- ")
                bsc_prch()
                break
            elif inter==4:
                print("\n----Your journey to the world of Economics---- ")
                bsc_prch()
                break
            elif inter==5:
                print("\n----Your journey to the world of Computer Science---- ")
                bsc_prch()
                break
            elif inter==6:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==7:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==8:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")
            

        elif res_12>=70 and res_12<75:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Mathematics:
                2. B.SC in Statistic:
                3. B.SC in Economics:
                4. B.SC in Computer Science:
                5. B.SC in Chemisty:
                6. B.SC in Electronics:
                7. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choice:"))

            if inter==1:
                print("\n----Your journey to the world of Mathematics---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Statistics---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journey to the world of Economics---- ")
                bsc_prch()
                break
            elif inter==4:
                print("\n----Your journey to the world of Computer Science---- ")
                bsc_prch()
                break
            elif inter==5:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==6:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==7:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=65 and res_12<70:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Statistic:
                2. B.SC in Economics:
                3. B.SC in Computer Science:
                4. B.SC in Chemisty:
                5. B.SC in Electronics:
                6. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))

            if inter==1:
                print("\n----Your journey to the world of Statistics---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Economics---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journey to the world of Computer Science---- ")
                bsc_prch()
                break
            elif inter==4:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==5:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==6:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=60 and res_12<65:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Economics:
                2. B.SC in Computer Science:
                3. B.SC in Chemisty:
                4. B.SC in Electronics:
                5. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))

            if inter==1:
                print("\n----Your journey to the world of Economics---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Computer Science---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==4:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==5:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=55 and res_12<60:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Computer Science:
                2. B.SC in Chemisty:
                3. B.SC in Electronics:
                4. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))
        
            if inter==1:
                print("\n----Your journey to the world of Computer Science---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==4:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=50 and res_12<55:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Chemisty:
                2. B.SC in Electronics:
                3. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))

            if inter==1:
                print("\n----Your journry to the world of Chemistry---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==3:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=45 and res_12<50:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Electronics:
                2. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))
        
            if inter==1:
                print("\n----Your journey to the world of Electronics---- ")
                bsc_prch()
                break
            elif inter==2:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12>=40 and res_12<45:
            print("\n ---Have you any interest like---")
            print("~"*40)
            print("""According to your score you are eligible for......
                
                1. B.SC in Biotechnology:""")
            
            inter = int(input("\n-> Enter your choise:"))
        
            if inter==1:
                print("\n----Your journey to the world of Biotechnology---- ")
                bsc_prch()
                break
            else:
                print("\n.....Wrong Input.Try again........:(!!!")


        elif res_12<=40 and res_12>=0:
            print("\n"+"~"*40)
            print(""".....Sorry not Eligible for BSC.....
            ".....Try something else..... """)
            print("~"*40)
            break
        

        else:
            print("\n.....Wrong Input.Try again.....:(!!!")