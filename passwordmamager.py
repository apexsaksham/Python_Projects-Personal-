


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            if "|" in line:
                data = line.rstrip()
                user, passw = data.strip().split("|")
                print("User: ", user , "Password: " ,passw)
        

def add():
    name = input("Enter the account name : ")
    pwd = input("Enter the password : ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + " \n ")


while True:
    mode  = input("Would you like to view existing password or add new ones ? (view/add/press q for quit) ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid input.")