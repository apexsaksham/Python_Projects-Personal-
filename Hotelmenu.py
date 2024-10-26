# Defining the menu
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}

print("Welcome to Python Restaurant!")
print("Here is the menu:")
print("Pizza  : Rs 40\nPasta  : Rs 50\nBurger : Rs 60\nSalad  : Rs 70\nCoffee : Rs 80")

order_total = 0

# First item
item1 = input("\nEnter the name of your item: ").lower()
if item1 in menu:
    order_total += menu[item1]
    print(f"Your {item1} has been ordered.")
else:
    print("Sorry, this item is not available.")

# Second item if the user wants to add more
another_order = input("Do you want to add another item? (Yes/No): ").lower()
if another_order == "yes":
    item2 = input("Enter the name of second item: ").lower()
    if item2 in menu:
        order_total += menu[item2]
        print(f"{item2.capitalize()} has been ordered.")
    else:
        print("Sorry, this item is not available.")

# Final total
print(f"\nThe total amount to pay for your order is Rs {order_total}.")
