import random

while True:
 choice = input("Roll the Dice? (y/n):  ").lower()
 if choice == "y":
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f" You rolled a {die1} and a {die2}")

 elif choice == "n":
    print("Thanks for playing")
    break
 else:
    print("Invalid choice")