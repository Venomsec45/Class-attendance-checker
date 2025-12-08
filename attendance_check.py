import os
from design import ascii_design

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
        name = input("Enter student name or type 'done' to exit: ").strip()

        if name.lower() == "done":
            break

        if name == "":
            print("Name cannot be empty" + "\n")

        elif name in students:
            print(f"{name} is already enrolled" + "\n")

        else:
            students.append(name)
            print(f"{name} added" + "\n")

    print("\nEnrollment complete" + "\n" + f"Number of enrolled students: {len(students)}")
    print("Enrolled students:")
    for index, student in enumerate(students, start=1):
        print(f"{index} - {student}")
    
    line()

# Record attendance
def record_attendance():
    clear()

    if not students:
        print("No students enrolled yet\n")
        return

    print("\n" + "RECORD ATTENDANCE".center(60, "-") + "\n")
    print("List of students:")
    for i, student in enumerate(students, start=1):
        print(f"{i} - {student}")
    
    print("\n")

    while True:
        name = input("Enter a student or type 'done' when finished: ").strip()

        if name.lower() == "done" and not present_students and not absent_students:
            print("Students not listed as present or absent")
            line()
            break

        if name.lower() == "done":
            for student in students:
                if student not in present_students and student not in absent_students:
                    absent_students.append(student)

            print("\nAttendance has been recorded\n" + "you may view the attendance on the 'view attendance' option")
            line()
            break

        if name not in students:
            print("Student is not in the enrolled list." + "\n")
            continue
        
        if name in present_students:
            print(f"{name} is already marked Present" + "\n")
            continue

        if name in absent_students:
            print(f"{name} is already marked Absent" + "\n")
            continue

        status = input("Enter 'present' or 'absent': ").strip().lower()

        if status == "present":
            present_students.append(name)
            print(f"{name} is marked as present" + "\n")

        elif status == "absent":
            absent_students.append(name)
            print(f"{name} is marked as absent" + "\n")

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
        view_input = input("\nCheck all, present or absent students (pr - present / ab - absent / a - all / d - to exit): ").lower().strip()

        if view_input == "pr":
            print("\nList of Present Students:")
            for index, present in enumerate(present_students, start=1):
                print(f"{index} - {present}")
            
        elif view_input == "ab":
            print("\nList of Absent Students:")
            for index, absent in enumerate(absent_students, start=1):
                print(f"{index} - {absent}")

        elif view_input == "a":
            print("\nList of All Students:")
            for index, student in enumerate(students, start=1):
                print(f"{index} - {student}")

        elif view_input == "d":
            line()
            break

        else:
            print("Choose one of the valid options\n")

# Search student status
def search_student_status():
    if not students and not present_students and not absent_students:
        print("No students in the lists!\n")
        return
    
    clear()
    print("SEARCH STUDENT".center(60, "-") + "\n")
    while True:
        search_input = input("Search student or type 'done' to exit: ").strip()

        if search_input.lower() == "done":
            line()
            break

        if search_input not in students:
            print("Student not in the list.")

        elif search_input in present_students:
            print(f"{search_input} is marked as Present.")

        elif search_input in absent_students:
            print(f"{search_input} is marked as Absent.")

# Download attendance
def download_attendance():
    clear()
    filename = "attendance_report.txt"

    if not students and not present_students and not absent_students:
        print("Student lists cannot be empty!\n")
        return

    with open(filename, "w") as file:
        file.write("Student Attendance Report".center(40, " "))
        file.write("-" * 40 + "\n")

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

if __name__ == "__main__":
    main()