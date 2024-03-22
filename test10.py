import random

result= random. randint(1,2)

guess = input("Enter head for 1 or Tril for 2 :")

if result == 1 and guess == 1:
    print ("You won. It's head")

elif result == 2 and guess ==2: 
    print("You won, It's Tail")

elif result == 1 and guess ==2: 
    print("You Lose, It's head")

elif result == 2 and guess ==1: 
    print("You Lose, It's Tail")

else: 
    print ("somthing went wrong. Try again")
