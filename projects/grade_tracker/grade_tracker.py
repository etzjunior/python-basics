students = {} # dictionary to store students infos

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
    name = input("Enter student mane to update: ").strip()
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

add_student()
add_student()
view_students()
show_stats()
update_students()
delete_student()
