students = {} # dictionary to store students infos

def add_student():
    # requests student names and grades from user
    names = input("Enter Student Name: ")
    grades = float(input("Enter Student Grades: "))

    students[names] = grades # adds student name and grades to the dictionary
    print(f"{names} added successfully!\n")

add_student()
add_student()

print("Current students dictionary:")
print(students)