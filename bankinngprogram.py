def show_balance(balance):
    print(f"Your balance is ${balance :.2f}")


def deposit():
    amount = float(input("Enter the amount you want ot deposit : "))
    if amount < 0:
        print("Please enter the valid amount")
    else:
        return amount

def withdraw(balance):
    withd = float(input("Enter the amount you want to withdraw : "))
    if withd > balance:
        print("Insufficient Balance")
        return 0 
    elif withd < 0:
        print("Invalid amount")
        return 0
    else:
        return withd


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1.Balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")

        choise = input("Enter your choice between (1-4) : ")
        if choise == "1":
            show_balance(balance)
        elif choise == "2":
            balance += deposit()
        elif choise == "3":
            balance -= withdraw(balance)
        elif choise == "4":
            is_running = False


if __name__ == '__main__':
    main()