from random import *
list=["rock","scissor","pepar"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
                        GAME START......
                        1.YES
                        2.NO
                  '''))
    if uc == 1:
        for a in range(1,6):
            userinput=int(input('''
                                    1. Rock
                                    2. Scissor
                                    3. Paper
                               '''))
            if userinput == 1:
                uchoice="rock"
                cchoice=choice(list)
            elif userinput == 2:
                uchoice="scissor"
                cchoice=choice(list)
            elif userinput == 3:
                uchoice="paper"
                cchoice=choice(list)
            if cchoice==uchoice:
               print("computer value: ",cchoice)
               print("your value: ",uchoice)
               print("game draw...")
            elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("computer value: ",cchoice)
                print("your value: ",uchoice)
                print("you win...")
                ucount=ucount+1
            else:
                print("computer value: ",cchoice)
                print("your value: ",uchoice)
                print("computer win...")
                ccount=ccount+1
            if ucount==ccount:
               print("finaly game draw.....")
               print("your score: ",ucount)
               print("computer score: ",ccount)
            elif ucount>ccount:
               print("finaly you win the game.....")
               print("your score: ",ucount)
               print("computer score: ",ccount)
            else:
                print("finaly computer win the game.....")
                print("your score: ",ucount)
                print("computer score: ",ccount)
    else:
        break