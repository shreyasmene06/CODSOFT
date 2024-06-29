import random
#GUESS MADE BY THE COMPUTER AND MATCHING IT WITH ANSWER
score_list=[]
def computer(value):
    global score_list
    answers=["rock","paper","scissors"]
    c=random.randint(0,2)                                       #chooses a random integer between 0 to 2
    pick=answers[c]                                             #uses that integer to choose an option from the list
    if value.strip().lower() in ("rock","paper","scissors"):     #checks if value entered by user is the following
        if pick==value.strip().lower():                         #checks if the guess is correct
            print("CONGRATULATIONS YOU GUESSED IT RIGHT!")
            print("==========================\n\n")
            score_list.append("Won")
        else:
            print("Better Luck Next Time :( ")
            print("==========================\n\n")
            score_list.append("Lost")
    else:
        print("invalid Value Entered Please Re-Enter")
        print("==========================\n\n")
        
def Score_tracker():
    global score_list
    if len(score_list)>0:
        print("=======SCORE TRACKER=======")
        for i in range(0,len(score_list)):
            print(f"GAME {i+1}. {score_list[i]}")
        print("==========================\n\n")
    else:
        print("No Games Played")

#MAIN FUNCTION WHICH MAKES SURE THAT THE PROGRAM RUNS 
def main():
    global score
    while True:
        
        ans=int(input('''PRESS 1 To Play The Game or PRESS 2 To Quit or PRESS 3 To View Score: '''))
        if ans==1:
            value=input("Choose Rock Paper or Scissors? : ")
            computer(value)
        elif ans==2:
            break
        elif ans==3:
            Score_tracker()


if __name__ == "__main__":
    main()