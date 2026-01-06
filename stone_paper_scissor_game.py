'''stone,paper,scissors'''

# 1- Rock
# 2- paper
# 3- scissors

import random 

comp_score=0
human_score=0

while True:
        if human_score == 5:
                print("you won the game congratulation")
                break
        if comp_score ==5:
                print("computer won the game")
                break
        you = int(input("press 1- for rock, press 2 for paper and press 3 for scissors:-"))
        if you >3 or you < 1:
                print("wrong input choose again")
                continue
        comp  = random.randint(1,3)
        if you == 1 and comp == 3:
                human_score+=1
                print(f"you won this round\ncurrent score- you - {human_score} and comp-{comp_score}")
        elif you ==2 and comp ==1:
                human_score+=1
                print(f"you won this round\ncurrent score- you - {human_score} and comp-{comp_score}")
        elif you ==3 and comp ==2:
                human_score+=1
                print(f"you won this round\ncurrent score- you - {human_score} and comp-{comp_score}")
        elif you == comp:
                print("its a draw")
                print(f"it was a draw\ncurrent score- you - {human_score} and comp-{comp_score}")
        else:
                comp_score= comp_score+1
                print(f"comp won this round\ncurrent score- you - {human_score} and comp-{comp_score}")        

