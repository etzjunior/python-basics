import json

students = {} # dictionary to store students infos

def load_students():
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}

def save_students():
    with open('students.json', 'w') as file:
        json.dump(students, file)


def add_student():
    # requests student names and grades from user
    names = input("Enter Student Name: ")
    grades = float(input("Enter Student Grades: "))

    students[names] = grades # adds student name and grades to the dictionary
    print(f"{names} added successfully!\n")


def view_students():
    if not students:        # checks if the students dictionary is empty
        print("No students available.\n")    
        return
    else:
        print("--- Student List ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")

def show_stats():    # shows highest, lowest and average grades
    if not students:
        print ("No Students Available!")
        return
    
    highest = max(students, key=students.get) 
    lowest = min(students, key=students.get)
    average = sum(students.values())/len(students)

    print("---Student Stats---")
    print(f"Highest: {highest} ({students[highest]})")
    print(f"Lowest: {lowest} ({students[lowest]})")
    print(f"Average: {average}")


def update_students():
    name = input("Enter student name to update: ").strip()
    if name in students:
        new_grade = float(input("Enter new grade: "))
        students[name] = new_grade
        print(f"{name}'s grade updated successfully!\n")
    else:
        print(f"{name} not found in the student list.\n")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"{name} deleted successfully!\n")
    else:
        print(f"{name} not found in the student list.")

print("1. Add Students")
print("2. View Students")
print("3. Show Stats")
print("4. Update Students")
print("5. Delete Students")
print("6. Exit")

Choice = input("Enter your choice (1-6): ")

if Choice == "1":
    add_student()
elif Choice == "2":
    view_students()
elif Choice == "3":
    show_stats()
elif Choice == "4":
    update_students()
elif Choice == "5":
    delete_student()
elif Choice == "6":
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 6.")


