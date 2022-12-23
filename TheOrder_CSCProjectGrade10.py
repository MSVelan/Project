print("                                            _ _ _ _   _   _ _              _ _ _    _ _     _ _ _     _ _     _ _")
print("                                               |     |__|  |_               |      |   |_ _}   |      \  |_      |_ _}")
print("                                               |     |    |  |_ _            |___|   |     \  _|_ _ /  |_ _   |    \ ")
#print the order
a=input("Press x to continue:")
while True:
        while a!='x':
            print("Invalid Input")
            a=input("Press x to continue:")
            if a=='x':
                break
        break
if a=='x':
        print("\nThis is a story of a YOUNG boy of the TOWN named BEACON TOWN.........")
        a=input("Press x to continue:")
        while True:
            while a!='x':
                print("TYPE X")
                a=input("Press x to continue:")
                if a=='x':
                    break
            break
        if a=='x':   
            print("\nYour character name:*JESSE*")      
            a=input("Press x to continue:")
            while True:
                while a!='x':
                    print("TYPE X")
                    a=input("Press x to continue:")
                    if a=='x':
                        break
                break
            if a=='x':
                print("\nJesse is a farmer kid, so he has to graze the cattle at the pasture ")
                a=input("Press x to continue:")
                while True:
                    while a!='x':
                        print("TYPE X")
                        a=input("Press x to continue:")
                        if a=='x':
                            break
                    break
                if a=='x':
                     print("\nSo help Jesse to finish his work")
                     import random
                     l=[]
                     print("Bulls --> letters matched in correct positions")
                     print("Cows --> letters matched in incorrect positions")
                     print("Crock --> letters do not match")
                     for i in range(3):
                         x=random.randint(97,122)
                         w=chr(x)
                         l.append(w)
                     a=l[0]
                     b=l[1]
                     c=l[2]
                     s=a+b+c
                     for j in range(20):
                            bulls=cows=0
                            m=input("Enter a three lettered word:")
                            if len(m)==3:
                                p=m[0]
                                q=m[1]
                                r=m[2]
                                if a==p and b==q:
                                   if c==r:
                                        print("Won")
                                        print("The generated word is:",s)
                                        break
                                if a!=p and b!=q and a!=q and a!=r and b!=p and b!=r:
                                    if c!=p and c!=q and c!=r:
                                        print("Crock")
                                for x in range(3):
                                        if m[x]==l[x]:
                                           bulls+=1
                                        elif m[x] in l:
                                            cows+=1
                                print("No. of cows=",cows)
                                print("No. of bulls=",bulls)
                     print("Generated word is:",s)
                     a=input("Press x to continue:")
                     while True:
                                while a!='x':
                                    print("TYPE X")
                                    a=input("Press x to continue:")
                                    if a=='x':
                                        break
                                break
                     if a=='x':
                                print("\nYou have done a great work!!!!!!")
                                a=input("Press x to continue:")
                                while True:
                                    while a!='x':
                                        print("TYPE X")
                                        a=input("Press x to continue:")
                                        if a=='x':
                                            break
                                    break
                                if a=='x':
                                    print("\nSo, the story of Jesse is a simple one.........")
                                    a=input("Press x to continue:")
                                    while True:
                                        while a!='x':
                                            print("TYPE X")
                                            a=input("Press x to continue:")
                                            if a=='x':
                                                break
                                        break
                                    if a=='x':
                                            print("\nJesse used to learn weapon specialization.....")
                                            a=input("Press x to continue:")
                                            while True:
                                                while a!='x':
                                                    print("TYPE X")
                                                    a=input("Press x to continue:")
                                                    if a=='x':
                                                        break
                                                break
                                            if a=='x':
                                                print("\nJesse used to craft his own sword ,bow and chains-mail armours.......")
                                                a=input("Press x to continue:")
                                                while True:
                                                    while a!='x':
                                                        print("TYPE X")
                                                        a=input("Press x to continue:")
                                                        if a=='x':
                                                            break
                                                    break
                                                if a=='x':
                                                    print("\nJesse used to excel in ...<-{|-~...BOW&ARROWS...~-|}->... and ...<===|=+...SWORD...+=|===>...  fights")
                                                    print("Jesse's friend name is *PETRA*")
                                                    a=input("Press x to continue:")
                                                    while True:
                                                        while a!='x':
                                                            print("TYPE X")
                                                            a=input("Press x to continue:")
                                                            if a=='x':
                                                                break
                                                        break
                                                    if a=='x':
                                                        print("\nSo after a few days, with Jesse and Petra roamed the town")   
                                                        a=input("Press x to continue:")
                                                        while True:
                                                            while a!='x':
                                                                print("TYPE X")
                                                                a=input("Press x to continue:")
                                                                if a=='x':
                                                                    break
                                                            break
                                                        if a=='x':
                                                            print("\nThe friends saw a strange path outside the town ")
                                                            a=input("Press x to continue:")
                                                            while True:
                                                                while a!='x':
                                                                    print("TYPE X")
                                                                    a=input("Press x to continue:")
                                                                    if a=='x':
                                                                        break
                                                                break
                                                            if a=='x':
                                                                print("\nHELP THE FRIENDS TO REACH THE OTHER SIDE!!!")
                                                                import random
                                                                m=45
                                                                z=m
                                                                while z==m:
                                                                    i=1
                                                                    l=[1,12,23,34,45,56,67,78,89,100]
                                                                    comp=0
                                                                    while i<11:
                                                                        choice=int(input("Enter ur input:"))
                                                                        if choice>comp and choice-comp<11:
                                                                            for j in range(1,11):
                                                                                for x in range(0,10):
                                                                                    if choice==l[x] and i!=10:
                                                                                        if j>1:
                                                                                            break
                                                                                        r=random.randint(1,10)
                                                                                        comp=choice+r
                                                                                        print("Computer's turn:",comp)
                                                                                        i+=1
                                                                                        break
                                                                                    elif choice+j==l[x]:
                                                                                        comp=l[x]
                                                                                        print("Computer's turn:",comp)
                                                                                        i+=1
                                                                                        break
                                                                            if choice==100:
                                                                                print("U won")
                                                                                m=47
                                                                                i+=1
                                                                            if comp==100:
                                                                                print("Comp won")
                                                                                i+=1
                                                                        else:
                                                                            print("Out of range")
                                                                            a=input("Press x to continue:")
                                                                            while True:
                                                                                while a!='x':
                                                                                    print("TYPE X")
                                                                                    a=input("Press x to continue:")
                                                                                    if a=='x':
                                                                                        break
                                                                                break
                                                                            if a=='x':
                                                                                 print("THAT WAS A STRANGE PATH INDEED!!!!!!")
                                                                                 a=input("Press x to continue:")
                                                                                 while True:
                                                                                     while a!='x':
                                                                                         print("TYPE X")
                                                                                         a=input("Press x to continue:")
                                                                                         if a=='x':
                                                                                            break
                                                                                     break
                                                                                 if a=='x':
                                                                                    print("\nTHE SCENE WAS STRANGE........")
                                                                                    a=input("Press x to continue:")
                                                                                    while True:
                                                                                        while a!='x':
                                                                                            print("TYPE X")
                                                                                            a=input("Press x to continue:")
                                                                                            if a=='x':
                                                                                                break
                                                                                        break
                                                                                    if a=='x':
                                                                                        print("\n............(O_O)         (O_O).............")
                                                                                        a=input("Press x to continue:")
                                                                                        while True:
                                                                                            while a!='x':
                                                                                                print("TYPE X")
                                                                                                a=input("Press x to continue:")
                                                                                                if a=='x':
                                                                                                    break
                                                                                            break
                                                                                        if a=='x':
                                                                                            print("\nThey saw a route into the ground.....")
                                                                                            a=input("Press x to continue:")
                                                                                            while True:
                                                                                                while a!='x':
                                                                                                    print("TYPE X")
                                                                                                    a=input("Press x to continue:")
                                                                                                    if a=='x':
                                                                                                        break
                                                                                                break
                                                                                            if a=='x':
                                                                                                print("\nTHEY heard a (*_*)SPOOKYSOUND(*_*).................")
                                                                                                a=input("Press x to continue:")
                                                                                                while True:
                                                                                                    while a!='x':
                                                                                                        print("TYPE X")
                                                                                                        a=input("Press x to continue:")
                                                                                                        if a=='x':
                                                                                                            break
                                                                                                    break
                                                                                                if a=='x':
                                                                                                    print("\nTHEY stumbled onto the large underground chamber")
                                                                                                    a=input("Press x to continue:")
                                                                                                    while True:
                                                                                                        while a!='x':
                                                                                                            print("TYPE X")
                                                                                                            a=input("Press x to continue:")
                                                                                                            if a=='x':
                                                                                                                break
                                                                                                        break
                                                                                                    if a=='x':
                                                                                                        print("\nBOOOOOOOOMMMM..........")
                                                                                                        a=input("Press x to continue:")
                                                                                                        while True:
                                                                                                            while a!='x':
                                                                                                                print("TYPE X")
                                                                                                                a=input("Press x to continue:")
                                                                                                                if a=='x':
                                                                                                                    break
                                                                                                            break
                                                                                                        if a=='x':
                                                                                                            print("\nIt was underground chamber ,with a sand pyramid in the middle.....")
                                                                                                            a=input("Press x to continue:")
                                                                                                            while True:
                                                                                                                while a!='x':
                                                                                                                    print("TYPE X")
                                                                                                                    a=input("Press x to continue:")
                                                                                                                    if a=='x':
                                                                                                                        break
                                                                                                                break
                                                                                                            if a=='x':
                                                                                                                print("\nThey saw the a PRISMARINE GLOVE in the middle of the pyramid.....")
                                                                                                                a=input("Press x to continue:")
                                                                                                                while True:
                                                                                                                    while a!='x':
                                                                                                                        print("TYPE X")
                                                                                                                        a=input("Press x to continue:")
                                                                                                                        if a=='x':
                                                                                                                            break
                                                                                                                    break
                                                                                                                if a=='x':
                                                                                                                    print("\nJESSE tried to look a closure look.....")
                                                                                                                    a=input("Press x to continue:")
                                                                                                                    while True:
                                                                                                                        while a!='x':
                                                                                                                            print("TYPE X")
                                                                                                                            a=input("Press x to continue:")
                                                                                                                            if a=='x':
                                                                                                                                break
                                                                                                                        break
                                                                                                                    if a=='x':
                                                                                                                        print("\n.............(l_l)              (l_l)..............")
                                                                                                                        a=input("Press x to continue:")
                                                                                                                        while True:
                                                                                                                            while a!='x':
                                                                                                                                print("TYPE X")
                                                                                                                                a=input("Press x to continue:")
                                                                                                                                if a=='x':
                                                                                                                                    break
                                                                                                                            break
                                                                                                                        if a=='x':
                                                                                                                            print("\nTHE GLOVE CLAMPS JESSE HANDS........")
                                                                                                                            a=input("Press x to continue:")
                                                                                                                            while True:
                                                                                                                                while a!='x':
                                                                                                                                    print("TYPE X")
                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                    if a=='x':
                                                                                                                                        break
                                                                                                                                break
                                                                                                                            if a=='x':
                                                                                                                                print("\nHE CANT GET IT OFF..............")
                                                                                                                                print("\nHE saw a no. flashed in his eyes (O_O)smtg(8525)(O_O)")
                                                                                                                                a=input("Press x to continue:")
                                                                                                                                while True:
                                                                                                                                    while a!='x':
                                                                                                                                        print("TYPE X")
                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                        if a=='x':
                                                                                                                                            break
                                                                                                                                    break
                                                                                                                                if a=='x':
                                                                                                                                    print("\nTHE SAND PYRAMID STARTED TO SHAKE.........")
                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                    while True:
                                                                                                                                        while a!='x':
                                                                                                                                            print("TYPE X")
                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                            if a=='x':
                                                                                                                                                break
                                                                                                                                        break
                                                                                                                                    if a=='x':
                                                                                                                                        print("\nThey got out of the underground chamber")
                                                                                                                                        print("\nBefore it was too late....................")
                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                        while True:
                                                                                                                                            while a!='x':
                                                                                                                                                print("TYPE X")
                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                if a=='x':
                                                                                                                                                    break
                                                                                                                                            break
                                                                                                                                        if a=='x':
                                                                                                                                            print("\nPetra told about someone who can help Jesse in the BEACON TOWN")
                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                            while True:
                                                                                                                                                while a!='x':
                                                                                                                                                    print("TYPE X")
                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                    if a=='x':
                                                                                                                                                        break
                                                                                                                                                break
                                                                                                                                            if a=='x':
                                                                                                                                                print("\nKNOCK!!! KNOCK!!!....................")
                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                while True:
                                                                                                                                                    while a!='x':
                                                                                                                                                        print("TYPE X")
                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                        if a=='x':
                                                                                                                                                            break
                                                                                                                                                    break
                                                                                                                                                if a=='x':
                                                                                                                                                    print("\nbehind the doors opened a adventurer named JACK")
                                                                                                                                                    print("AND THE GUY  NAMED NURM who was his personal guide and a true friend of him..........")
                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                    while True:
                                                                                                                                                        while a!='x':
                                                                                                                                                            print("TYPE X")
                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                            if a=='x':
                                                                                                                                                                break
                                                                                                                                                        break
                                                                                                                                                    if a=='x':
                                                                                                                                                        print("\nJack by the way was a legendary treasure hunter")
                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                        while True:
                                                                                                                                                            while a!='x':
                                                                                                                                                                print("TYPE X")
                                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                                if a=='x':
                                                                                                                                                                    break
                                                                                                                                                            break
                                                                                                                                                        if a=='x':
                                                                                                                                                            print("\nJack was visibly shocked to see the gauntlet, ")
                                                                                                                                                            print("\nHe said that it is one of his powerful creation!!!!")
                                                                                                                                                            print("\nNurm mentions that it belongs to the admin")
                                                                                                                                                            print("\nAnd also said, it is used to decode or defragment the admin who created the world")
                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                            while True:
                                                                                                                                                                while a!='x':
                                                                                                                                                                    print("TYPE X")
                                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                                    if a=='x':
                                                                                                                                                                        break
                                                                                                                                                                break
                                                                                                                                                            if a=='x':
                                                                                                                                                                print("\nThe gauntlet is a key to unlock 2 structure blocks")
                                                                                                                                                                print("\nLOCATED IN THE (._.)OCEAN MONUMENT(._.)")
                                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                                while True:
                                                                                                                                                                    while a!='x':
                                                                                                                                                                        print("TYPE X")
                                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                                        if a=='x':
                                                                                                                                                                            break
                                                                                                                                                                    break
                                                                                                                                                                if a=='x':
                                                                                                                                                                    print("\nSo they set adventure for a !!!voyage!!!")
                                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                                    while True:
                                                                                                                                                                        while a!='x':
                                                                                                                                                                            print("TYPE X")
                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                            if a=='x':
                                                                                                                                                                                break
                                                                                                                                                                        break
                                                                                                                                                                    if a=='x':
                                                                                                                                                                        print("\nThe guys were preparing their essentials for the trip")
                                                                                                                                                                        print("\nThe OCEAN MONUMENT was hidden beneath the OCEAN")
                                                                                                                                                                        print("\nSO THE ADMIN CREATED IT JUST THE WAY SUCH THAT NO WATER ENTERS IT")
                                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                                        while True:
                                                                                                                                                                            while a!='x':
                                                                                                                                                                                print("TYPE X")
                                                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                                                if a=='x':
                                                                                                                                                                                    break
                                                                                                                                                                            break
                                                                                                                                                                        if a=='x':
                                                                                                                                                                            print("\nThe guys reached the monument ,and the guys saw a code to open the door")
                                                                                                                                                                            print("IT MENTIONED CORRECT COMBINATION FOR  .....($_$)OPEN SESAME($_$).....")
                                                                                                                                                                            print("___________")
                                                                                                                                                                            print("||||| ...... |||||")
                                                                                                                                                                            print("||||| ...... |||||")
                                                                                                                                                                            print("| 1 | | 2 | | 3 |")
                                                                                                                                                                            print("| 4 | | 5 | | 6 |")
                                                                                                                                                                            print("| 7 | | 8 | | 9 |")
                                                                                                                                                                            print("----------------")
                                                                                                                                                                        a=input("ENTER YOUR COMBINATION:")
                                                                                                                                                                        while True:
                                                                                                                                                                            while a!='8525':
                                                                                                                                                                                print("Invalid Combimnation")
                                                                                                                                                                                a=input("Enter your combination:")
                                                                                                                                                                                if a=='8525':
                                                                                                                                                                                    break
                                                                                                                                                                            break
                                                                                                                                                                        if a=='8525':
                                                                                                                                                                            print("\n(!_!)!!THE MONUMENT OPENS!!(!_!)")
                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                            while True:
                                                                                                                                                                                while a!='x':
                                                                                                                                                                                    print("TYPE X")
                                                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                                                    if a=='x':
                                                                                                                                                                                        break
                                                                                                                                                                                break
                                                                                                                                                                            if a=='x':
                                                                                                                                                                                print("\nIT SHOWED THE SIGN OF")
                                                                                                                                                                                print(" _           _   _ _                _ _ _      _ _     _     _   _ _ ")
                                                                                                                                                                                print("  \    /\    /   I _     I           I           I       I    I \ / I   I _")                                                 
                                                                                                                                                                                print("    \/    \/     I_ _   I_ _ _   I_ _ _   I _ _ I    I      I   I_ _ ")
                                                                                                                                                                                print("IN A BIG BANNER..........")
                                                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                                                while True:
                                                                                                                                                                                    while a!='x':
                                                                                                                                                                                        print("TYPE X")
                                                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                                                        if a=='x':
                                                                                                                                                                                            break
                                                                                                                                                                                    break
                                                                                                                                                                                if a=='x':
                                                                                                                                                                                    print("THE GUYS SAW  PRISMARINE MONUMENT GAURDS")
                                                                                                                                                                                    print("SO THE guys drawed their sword out and exclaimed FIGHT!!!!!!!!!!!!!")
                                                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                                                    while True:
                                                                                                                                                                                        while a!='x':
                                                                                                                                                                                            print("TYPE X")
                                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                                            if a=='x':
                                                                                                                                                                                                break
                                                                                                                                                                                        break
                                                                                                                                                                                    if a=='x':
                                                                                                                                                                                            print("\nMODE OF FIGHT:")
                                                                                                                                                                                            m=input("BOW OR SWORD:")
                                                                                                                                                                                            if m=='BOW' or m=='bow' or m=='Bow':
                                                                                                                                                                                                               print("YOUR  MODE OF SELECTION IS ...~-|}->....")
                                                                                                                                                                                            elif m=='SWORD' or m=='sword' or m=='Sword' :
                                                                                                                                                                                                               print("YOUR  MODE OF SELECTION IS ....<===|=+....")
                                                                                                                                                                                            while True:
                                                                                                                                                                                                        while m!='BOW' and m!='bow' and m!='Bow' and m!='SWORD' and m!='sword' and m!='Sword' :
                                                                                                                                                                                                               print("Invalid input")
                                                                                                                                                                                                               m=input("TYPE MOF CHOICE:")
                                                                                                                                                                                                               if m=='BOW' or m=='bow' or m=='Bow':
                                                                                                                                                                                                                               print("YOUR  MODE OF SELECTION IS ...~-|}->....")
                                                                                                                                                                                                                               a=input("Press x to (+)SHOOT(+) the TARGET :")
                                                                                                                                                                                                                               while True:
                                                                                                                                                                                                                                        while a!='x':
                                                                                                                                                                                                                                            print("TYPE x THE ENEMIES ARE APPROACHING")
                                                                                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                                                                                            if a=='x':
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                               if a=='x':
                                                                                                                                                                                                                                        print("\nSTHHHHH THE GAURDS WERE FALLEN!!")
                                                                                                                                                                                                               elif m=='SWORD' or m=='sword' or m=='Sword' :
                                                                                                                                                                                                                               print("YOUR  MODE OF SELECTION IS ....<===|=+....")
                                                                                                                                                                                                                               a=input("Press x to (+=|===>)STAB(<===|=+) the TARGET :")
                                                                                                                                                                                                                               while True:
                                                                                                                                                                                                                                        while a!='x':
                                                                                                                                                                                                                                            print("TYPE x THE ENEMIES ARE APPROACHING")
                                                                                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                                                                                            if a=='x':
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                               if a=='x':
                                                                                                                                                                                                                                        print("\nOof THE GAURDS WERE FALLEN!!")
                                                                                                                                                                                                                               break
                                                                                                                                                                                                        a=input("Press x to continue:")
                                                                                                                                                                                                        while True:
                                                                                                                                                                                                                while a!='x':
                                                                                                                                                                                                                    print("TYPE X")
                                                                                                                                                                                                                    a=input("Press x to continue:")
                                                                                                                                                                                                                    if a=='x':
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                break
                                                                                                                                                                                                        if a=='x':
                                                                                                                                                                                                                print("\nTHE ADMIN APPEARED ................")
                                                                                                                                                                                                                print("\nAND FOUND THE MESS DONE HERE BY JESSE AND HIS FRIENDS...")
                                                                                                                                                                                                                print("\nHE WAS ANGRY AND HE EXCLAIMED......")
                                                                                                                                                                                                                print("\nHE WILL DESTROY THIS WORLD....")
                                                                                                                                                                                                                a=input("Press x to continue:")
                                                                                                                                                                                                                while True:
                                                                                                                                                                                                                        while a!='x':
                                                                                                                                                                                                                            print("TYPE X")
                                                                                                                                                                                                                            a=input("Press x to continue:")
                                                                                                                                                                                                                            if a=='x':
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                if a=='x':
                                                                                                                                                                                                                        print("\nSuddenly JESSE HIT THE ADMIN WITH HIS GLOVE....")
                                                                                                                                                                                                                        print("\nNOW THE ADMIN IS TEMPORARY <<UNFUNCTIONABLE>>")
                                                                                                                                                                                                                        import random
                                                                                                                                                                                                                        a=str(random.randint(0,9))
                                                                                                                                                                                                                        b=str(random.randint(0,9))
                                                                                                                                                                                                                        c=str(random.randint(0,9))
                                                                                                                                                                                                                        d=str(random.randint(0,9))
                                                                                                                                                                                                                        print("(?,?,?,?) \nDECODE the ADMIN FAST!!!!!YOU HAVE 10 CHANCES")
                                                                                                                                                                                                                        pas=(a,b,c,d)
                                                                                                                                                                                                                        for i in range(1,11):
                                                                                                                                                                                                                            k=input(" \nEnter the DECODE:")
                                                                                                                                                                                                                            p=k[0]
                                                                                                                                                                                                                            q=k[1]
                                                                                                                                                                                                                            r=k[2]
                                                                                                                                                                                                                            s=k[3]
                                                                                                                                                                                                                            if p==a  and q==b and r==c and s==d:
                                                                                                                                                                                                                                print("\nTHE ADMIN IS DEFRAGMENTED AND JESSE GOT THE ADMIN'S POWER")
                                                                                                                                                                                                                                print("Password:--",k)
                                                                                                                                                                                                                                print("\nJESSE NOW SAVED THE WORLD AND CREATED A MORE BEAUTIFUL WORLD")
                                                                                                                                                                                                                                print("\nHE UNLOCKED THE POWER OF DIMENSIONS........")
                                                                                                                                                                                                                                print("\nSO THESE GUYS SET OUT FOR ANOTHER ADVENTURE!!!!!!!!")
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            if a==p:
                                                                                                                                                                                                                                print(a,end=' ')
                                                                                                                                                                                                                            if p!=a:
                                                                                                                                                                                                                                print("_",end=' ')
                                                                                                                                                                                                                            if b==q:
                                                                                                                                                                                                                                print(b,end=' ')
                                                                                                                                                                                                                            if q!=b:
                                                                                                                                                                                                                                print("_",end=' ')
                                                                                                                                                                                                                            if c==r:
                                                                                                                                                                                                                                print(c,end=' ')
                                                                                                                                                                                                                            if r!=c:
                                                                                                                                                                                                                                print("_",end=' ')
                                                                                                                                                                                                                            if d==s:
                                                                                                                                                                                                                                print(d,end=' ')
                                                                                                                                                                                                                            if s!=d:
                                                                                                                                                                                                                                print("_")
                                                                                                                                                                                                                            if p!=a and q!=b and r!=c and s!=d:
                                                                                                                                                                                                                                print("\nNone of them are in correct position")
                                                                                                                                                                                                                           
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            print("DECODING FAILURE!!!!!")
                                                                                                                                                                                                                            print("Password:--",str(a+b+c+d))
                                                                                                                                                                                                                            print("\nADMIN GOT UP FROM THE STUNT AND HE DESTROYED THE WORLD")
                                                                                                                                                                                                                            print("\n(;_;)YOUR STORY ENDS HERE(;_;).........")
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                            

                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                                                                


   
