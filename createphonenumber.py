import random
create_phone_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

while True:
    choices = input("Want to create a number ? (yes/no): ")
    if choices.lower() == "yes":
        area = random.randint(100, 999)
        central = random.randint(100, 999)
        line = random.randint(1000, 9999)

        phone_number = f"({area}) {central} -- {line}"
        print(f"Your number is created {phone_number}")

    else:
        print("Thanks")
        break