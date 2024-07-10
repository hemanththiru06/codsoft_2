def rps(opp,you):
    if opp==you:
        print("TIE")
    elif opp=='rock':
        if you=='paper':                
            print("You WON")
        elif you=='scissor':
            print("Computer WON")
    elif opp=='paper':
        if you=='rock':
            print("Computer WON")
        elif you=='scissor':
            print("You WON")
    else:
        if you=='paper':
            print("Computer WON")
        elif you=='rock':
            print("You WON")
    return

import random
while True:
    options=['rock','paper','scissor']
    computer=random.choice(options)
    user=input("Choose rock or paper or scissor:").lower()
    if user not in options:
        print ("Invalid option choose again")
        continue
    print("Computer's choice:",computer)
    print("User choice:",user)
    rps(computer,user)
    i=int(input("play again? \nPress 0 to play and 1 to exit:"))
    if i==1:
        break
