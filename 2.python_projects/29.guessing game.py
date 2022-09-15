import random
print("you will get 5 chances to choose -----")
for x in range (1,5+1):
    guessNumber = int(input("enter a number between 1 t o 5 :"))
    randomNumber = random.randint(1, 5)
    if guessNumber == randomNumber:
        print("guessed number matched ", randomNumber)
        break
    else:
        print("you have lost" + " random number was", randomNumber)
