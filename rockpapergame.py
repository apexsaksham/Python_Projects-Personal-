import random
import emojis

rock = "\U0001FAA8"  # 🪨
paper = "\U0001F4C4"  # 📃
scissors = "\u2702"   # ✂️

emoji = {"r" : rock, "s" : scissors, "p" : paper }

choices = ('r','p','s')

while True:
    user_choice = input("Rock, Paper or Scissors : (r,p,s) :").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose : {emoji[user_choice]}")
    print(f"computer chose : {emoji[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie")

    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "s" and computer_choice == "p") or (user_choice == "p" and computer_choice == "r"):
        print("You win")

    else:
        print("You lost")

    cont = input("Would you like to continue (y/n): ")
    if cont == "n":
        break