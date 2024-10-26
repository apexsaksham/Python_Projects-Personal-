def task():
    tasks = []  #empty list
    print("______Welcome to TO DO LIST______")

    
    total_task = int(input("How many tasks you wants to add : " ))
    for i in range(1, total_task+1):
        taskname = input(f"enter tasks {i} : ")
        tasks.append(taskname)

    print(f"Todays tasks are\n{tasks}")    

    while True:
        operation = int(input("press 1- add\npress 2- update\npress 3- delete\npress 4- view\npress 5- exit/stop : "))
        if operation == 1:
            add = input("Enter the task you want to add : ")
            tasks.append(add)
            print(f"your task {add} has been added")

        elif operation == 2:
            updatedtask = input("Enter the task you want to update : ")
            if updatedtask in tasks:
                up = input("enter new task : ")
                ind = tasks.index(updatedtask)    # finding the given task to replace
                tasks[ind] = up # updated by new task
                print(f"task {up} has be updated")

        elif operation == 3:
            delvalue = input("Enter the task you want ot delete : ")
            if delvalue in tasks:
                ind = tasks.index(delvalue)    #finding the value to be deleted
                del tasks[ind]     # deleting the value
                print(f"Task {delvalue } has been deleted")

        elif operation == 4:
            print(f"Total tasks {tasks}")


        elif operation == 5:
            print("closing the program")
            break        
        
        else:
            print("invalid input")



task()  # calling the function