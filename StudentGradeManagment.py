student_grades = {}


def add_student(name, grades):
    student_grades[name] = grades
    print(f"Added {name} with grades: {grades}")


def update_student(name, grades):
    if name in student_grades:
        student_grades[name] = grades
        print(f"{name}'s grades have been updated to {grades}")
    else:
        print(f"{name} is not found")


def del_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} has been deleted")
    else:
        print(f"{name} is not found")


def display_all():
    if student_grades:
        for name, grades in student_grades.items():
            print(f"{name}: {grades}")
    else:
        print("No students found")


def main():
    while True:
        print("\nStudent Grade Management")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Display students")
        print("5. Exit")
    
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            name = input("Enter the name of the student: ")
            grades = int(input("Enter the grades of the student: "))
            add_student(name, grades)
    
        elif choice == 2:
            name = input("Enter the name of the student: ")
            grades = int(input("Enter the new grades: "))
            update_student(name, grades)
    
        elif choice == 3:
            name = input("Enter the name of the student: ")
            del_student(name)
    
        elif choice == 4:
            display_all()
    
        elif choice == 5:
            print("Exiting...")
            break
    
        else:
            print("Invalid input")


# Call the main function to run the program
main()
