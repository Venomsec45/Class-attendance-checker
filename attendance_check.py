import os
from design import ascii_design # ascii art

# Clearing the terminal
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Border line
def line():
    print("\n" + "-" * 60 + "\n")

# Lists of students
students = []
present_students = []
absent_students = []

# Enroll students
def enroll_students():
    clear()

    print("\n" + "ENROLL STUDENTS".center(60, "-") + "\n")
    while True:
        # User should type a student's name or done to exit and proceed to the main menu
        name = input("Enter student name or type 'done' to exit: ").strip()

        if name.lower() == "done":
            break

        # name cannot be blank
        if name == "":
            print("Name cannot be empty" + "\n")

        # If student's name is on the student list, the program tells the user that a name has already been added
        elif name in students:
            print(f"{name} is already enrolled" + "\n")

        # Adds the student's name to the student list
        else:
            students.append(name)
            print(f"{name} added" + "\n")

    # It shows the number of enrolled students and the enrolled students
    print("\nEnrollment complete" + "\n" + f"Number of enrolled students: {len(students)}")
    print("Enrolled students:")
    for index, student in enumerate(students, start=1):
        print(f"{index} - {student}")
    
    line()

# Record attendance
def record_attendance():
    clear()

    # It prompts the user to enroll a student
    if not students:
        print("No students enrolled yet\n")
        return

    # It shows the lists of students before the user records the attendance
    print("\n" + "RECORD ATTENDANCE".center(60, "-") + "\n")
    print("List of students:")
    for i, student in enumerate(students, start=1):
        print(f"{i} - {student}")
    
    print("\n")

    while True:
        # The user enters a name
        name = input("Enter a student or type 'done' when finished: ").strip()

        # The program tells the user that there are no students in the list
        if name.lower() == "done" and not present_students and not absent_students:
            print("Students not listed as present or absent")
            line()
            break

        # Automatically marks the non included students as absent
        if name.lower() == "done":
            for student in students:
                if student not in present_students and student not in absent_students:
                    absent_students.append(student)
                
            print("\nAttendance has been recorded\n" + "you may view the attendance on the 'view attendance' option")
            line()
            break

        # If a student doesn't exist
        if name not in students:
            print("Student is not in the enrolled list." + "\n")
            continue
        
        # If the student is already in the present student list
        if name in present_students:
            print(f"{name} is already marked Present" + "\n")
            continue

        # If the student is already in the absent student list
        if name in absent_students:
            print(f"{name} is already marked Absent" + "\n")
            continue

        # Prompts the user to enter present or absent
        status = input("Enter 'present' or 'absent': ").strip().lower()

        if status == "present":
            present_students.append(name)
            print(f"{name} is marked as present" + "\n")

        elif status == "absent":
            absent_students.append(name)
            print(f"{name} is marked as absent" + "\n")

        # If the user enters different input
        else:
            print("Enter whether the student is 'present' or 'absent' and try again!" + "\n")
            
# View attendance
def view_attendance():
    clear()
    if not present_students and not absent_students and not students:
        print("No students in the list!\n")
        return

    print("VIEW ATTENDANCE".center(60, "-"))
    while True:
        # The program prompts the user to choose the following categories
        view_input = input("\nCheck all, present or absent students (pr - present / ab - absent / a - all / d - to exit): ").lower().strip()

        # Shows the list of present students
        if view_input == "pr":
            print("\nList of Present Students:")
            for index, present in enumerate(present_students, start=1):
                print(f"{index} - {present}")
            
        # Shows the list of absent students
        elif view_input == "ab":
            print("\nList of Absent Students:")
            for index, absent in enumerate(absent_students, start=1):
                print(f"{index} - {absent}")

        # Shows the list of all students
        elif view_input == "a":
            print("\nList of All Students:")
            for index, student in enumerate(students, start=1):
                print(f"{index} - {student}")

        # To move to the main menu
        elif view_input == "d":
            line()
            break

        # When the user enters a different input
        else:
            print("Choose one of the valid options\n")

# Search student status
def search_student_status():
    if not students and not present_students and not absent_students:
        clear()
        print("No students in the lists!\n")
        return
    
    clear()
    print("SEARCH STUDENT".center(60, "-") + "\n")
    while True:
        # Search a student or ttype done to move to the main menu
        search_input = input("Search student or type 'done' to exit: ").strip()

        if search_input.lower() == "done":
            line()
            break

        # If a student doesn't exist
        if search_input not in students:
            print("Student not in the list.")

        # If a student is present
        elif search_input in present_students:
            print(f"{search_input} is marked as Present.")

        # If a student is absent
        elif search_input in absent_students:
            print(f"{search_input} is marked as Absent.")

# Download attendance
def download_attendance():
    clear()
    filename = "attendance_report.txt"

    # Tells the user that an empty list cannot be imported to a file
    if not students and not present_students and not absent_students:
        print("Student lists cannot be empty!\n")
        return

    # Imports all the list of present, absent and all students in a file
    with open(filename, "w") as file:
        file.write("Student Attendance Report".center(40, " "))
        file.write("\n" + "-" * 40 + "\n")

        file.write("Enrolled Students:\n")
        for i, s in enumerate(students, start=1):
            file.write(f"{i} - {s}\n")

        file.write("\nPresent Students:\n")
        for i, p in enumerate(present_students, start=1):
            file.write(f"{i} - {p}\n")

        file.write("\nAbsent Students:\n")
        for i, a in enumerate(absent_students, start=1):
            file.write(f"{i} - {a}\n")

    print(f"\nAttendance saved to '{filename}'" + "\n")

# Main program
def main():
    clear()
    ascii_design()

    choices = {
        "1": enroll_students,
        "2": record_attendance,
        "3": view_attendance,
        "4": search_student_status,
        "5": download_attendance,
        "6": exit,
    }

    try:
        while True:
            print("1. Enroll Students")
            print("2. Record Attendance")
            print("3. View Attendance Report")
            print("4. Search Student Status")
            print("5. Download Attendance File")
            print("6. Exit Program")

            choice = input("\nChoose an option (1-6): ").strip()

            if choice in choices:
                choices[choice]()
            else:
                print("Choose one of the following options and try again!\n")

    except KeyboardInterrupt:
        print("\nAttendance checking cancelled.")

# Ensures that the program is not run as a module from another code
if __name__ == "__main__":
    main()