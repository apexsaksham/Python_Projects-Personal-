print("Welcome to computer quiz")

playing = input("Do you wanna play ? :) (Yes/no) ").lower()

if playing == "no":
    quit()

print("Okay lets play")
score = 0

answer = input("What does Cpu stands for ?  : ")
if answer == "central processing unit".lower():
    print("Correct")
    score = score+1
    print(f"your score is {score} ") 
else:
    print("Incorrect")


# Question 1
answer = input("What does RAM stand for? : ")
if answer == "random access memory".lower():
    print("Correct")
    score = score+1
    print(f"your score is {score} ")  
else:
    print("Incorrect")

# Question 2
answer = input("What does HTTP stand for? : ")
if answer == "hypertext transfer protocol".lower():
    print("Correct")
    score = score+1
    print(f"your score is {score} ")
else:
    print("Incorrect")

# Question 3
answer = input("What does HTML stand for? : ")
if answer == "hypertext markup language".lower():
    print("Correct")
    score = score+1
    print(f"your score is {score} ")   (f"your score is {score} ")
else:
    print("Incorrect")

# Question 4
answer = input("What does IP stand for? : ")
if answer == "internet protocol".lower():
    print("Correct")
    score = score+1
    print(f"your score is now {score} ")
else:
    print("Incorrect")


