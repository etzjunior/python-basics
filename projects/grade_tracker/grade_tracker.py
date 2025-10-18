students = {} # dictionary to store students infos

def add_student():
    # requests student names and grades from user
    names = input("Enter Student Name: ")
    grades = float(input("Enter Student Grades: "))

    students[names] = grades # adds student name and grades to the dictionary
    print(f"{names} added successfully!\n")


def view_students():
    if not students:
        print("No students available.\n")
    else:
        print("--- Student List ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")


print("Current students dictionary:")
print(students)

add_student()
add_student()
view_students()
