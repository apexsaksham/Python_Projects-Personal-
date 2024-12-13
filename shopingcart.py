foods = []
prices = []
total_price = 0

while True:
    food = input("Enter the food you want to buy or press q to quit :")
    if food.lower() == "q":
        break
    else:
       price = float(input("Enter the price of your food : $"))
       foods.append(food)
       prices.append(price)
       total_price += price


print("----YOUR CART----")

for food in foods:
     print(f"{food}  ", end= " ")

# for price in prices:
#     total_price += price
print(f"Your total bill is {total_price}")
