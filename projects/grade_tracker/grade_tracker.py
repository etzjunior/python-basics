import json
import csv

students = {} # dictionary to store students infos

def load_students():
    global students
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}

def save_students():
    global students
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

load_students() # load existing student data from file

def add_student():
    # requests student names and grades from user
    names = input("Enter Student Name: ").strip()

    if not names:
        print("Student name cannot be empty.\n")
        return
    if names in students:
        print(f"{names} already exists. Use update option to change the grade.\n")
        return
    try:
        grades = float(input("Enter Student Grade (0–100): "))
        if grades < 0 or grades > 100:
            print("Grade must be between 0 and 100.\n")
            return
    except ValueError:
        print("Invalid grade. Please enter a numeric value.\n")
        return

    students[names] = grades # adds student name and grades to the dictionary
    save_students() # saves updated student data to file
    print(f"{names} added successfully!\n")


def view_students():
    if not students:        # checks if the students dictionary is empty
        print("No students available.\n")    
        return
    else:
        print("--- Student List ---")
        for name, grade in students.items():
            letter = get_letter_grade(grade)
            print(f"{name}: {grade}({letter})")

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


def update_students():   # updates a student's grade
    name = input("Enter student name to update: ").strip()
    if name not in students:
        print(f"{name} not found in the student list.\n")
        return
    try:
        new_grade = float(input("Enter new grade (0–100): "))
        if new_grade < 0 or new_grade > 100:
            print("Grade must be between 0 and 100.\n")
            return
    except ValueError:
        print("Invalid grade. Please enter a numeric value.\n")
        return
    students[name] = new_grade
    save_students()
    print(f"{name}'s grade updated successfully!\n")
 

def delete_student():   # deletes a student from the dictionary
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        save_students()
        print(f"{name} deleted successfully!\n")
    else:
        print(f"{name} not found in the student list.")


def search_students():   # searches for students by name
    query = input("Enter student name to search:").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    
    results = {name: grade for name, grade in students.items() if query in name.lower()}

    if results:
        print("--- Search Results ---")
        for name,grade in results.items():
            letter = get_letter_grade(grade)
            print(f"{name}: {grade}({letter})")
    else:
        print("No matching students found.")

def sort_students():  # sorts students by name or grade
    if not students:
        print("No students available to sort.")
        return
    print("Sorting options:")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Grade (High to Low)")

    choice = input("Enter your choice (1-2):").strip()
    if choice == "1":
        sorted_list = sorted(students.items())
    elif choice =="2":
        sorted_list = sorted(students.items(), key=lambda x: x[1], reverse=True)
    else:
        print("Invalid choice, please enter 1 or 2.\n")
        return
    print("--- Sorted Students ---")
    for name, grade in sorted_list:
        letter = get_letter_grade(grade)
        print(f"{name}: {grade}({letter})")
    print()
    
def export_to_csv():  # exports student data to a CSV file
    if not students:
        print("No students available to export.")
        return
    filename = "students.csv"

    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grade", "Letter Grade"])
        for name, grade in students.items():
            letter = get_letter_grade(grade)
            writer.writerow([name, grade, letter])
    print(f"Students data successfully exported to {filename}\n")


while True:    # main menu loop
    print("1. Add Students")
    print("2. View Students")
    print("3. Show Stats")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Search Students")
    print("7. Sort Students")
    print("8. Export to CSV")
    print("9. Exit")

    Choice = input("Enter your choice (1-9): ") # gets user choice

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
        search_students()
    elif Choice == "7":
        sort_students()
    elif Choice == "8":
        export_to_csv()
    elif Choice == "9":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")





