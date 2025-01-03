MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Plaese enter the valid digit")


    return amount 


def get_number_lines():
    while True:
        lines = input("Enter the the number of lines to bet (1- " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number")
        else:
            print("Plaese enter the valid digit")


    return lines     


def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Plaese enter the valid digit")


    return amount 



def main():
    balance = deposit()
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have to bet because you total balance is low. Balance is  ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} . total bet is equals to ${total_bet}")

   


main()