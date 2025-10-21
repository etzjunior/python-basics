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

add_student()
add_student()
view_students()
show_stats()
