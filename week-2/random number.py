import random

n=random.randint(1,100)
print("\tGUESS THE NUMBER\n")
print("\tyou have 6 chances")
x=1
while(x<=6):
    guess=int(input("guess the number: "))
    if guess==n:
        print("you won")
        break
    elif x==6:
    	print("\tyour chances are over")
    	print("\t\tTRY AGAIN")
    	break
    elif guess<n:
        print("your guess is low")
        x+=1
    elif guess<n:
        print("your guess is high")
        x+=1
