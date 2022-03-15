import random
n= 20
random_guessed = int(n * random.random()) + 1 # it will create random number 0 to 20:
guess = 0

while guess != random_guessed:
    guess = int(input("New guess number: "))
    if guess > 0:
        if guess > random_guessed:
            print("Number is large")
        
        elif guess < random_guessed:
            print("Number is small: ")   

    else:
        print("Sorry that you are giving up")
        break
else:
    print("Congratulation, You made it!")