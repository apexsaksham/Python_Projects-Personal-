import random
number = random.randint(1, 101)
while True:
    x = input("Guess the number from 1 to 100 : ")
    choice = int(x)
 

    if choice < number:
        print("Too low number ")

    elif choice > number:
        print("Too high number ")

    elif choice == number:
        print("Congrats! You've guessed the number")
        break
    
