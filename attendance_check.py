import os

def text_design():
    print("-" * 60)
    print("Student attendance checker".center(60, "="))
    print("-" * 60)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Lists of students
students = []
present_students = []
absent_students = []

# Enroll students
def enroll_students():
    global students
    students = []

    while True:
        print("\n" + "Enroll Students".center(60, "-") + "\n")
        name = input("Enter student name or type 'done' to exit: ").strip()

        if name.lower() == "done":
            break

        if name == "":
            print("Name cannot be empty.")

        elif name in students:
            print(f"{name} is already enrolled.")

        else:
            students.append(name)
            print(f"{name} added")

    print("\nEnrollment complete" + "\n" + f"Number of enrolled students: {len(students)}")
    print("Enrolled students:")
    for index, student in enumerate(students, start=1):
        print(f"{index} - {student}")

# Record attendance
def record_attendance():
    clear()
    global present_students, absent_students

    if not students:
        print("\nNo students enrolled yet.")
        return

    present_students = []
    absent_students = []

    print("\n" + "Record Attendance".center(60, "-") + "\n")
    print("List of students")
    for i, student in enumerate(students, start=1):
        print("+" + "-" * 40 + "+")

    while True:
        name = input("Enter a student or type 'done' when finished: ").strip()

        if name.lower() == "done":
            break

        if name not in students:
            print("Student is not in the enrolled list.")
            continue
        
        if name in present_students:
            print(f"{name} is already marked Present")
            continue

        if name in absent_students:
            print(f"{name} is already marked Absent")
            continue

        status = input("Enter 'present' or 'absent': ").strip().lower()

        if status == "present":
            present_students.append(name)
            print(f"{name} is marked as present")

        elif status == "absent":
            absent_students.append(name)
            print(f"{name} is marked as absent")

        else:
            print("Enter whether the student is 'present' or 'absent' and try again!")

    for student in students:
        if student not in present_students and student not in absent_students:
            absent_students.append(student)

    print("\nAttendance has been recorded, you may view the attendance on the 'view attendance' option")

# View attendance
def view_attendance():
    clear()
    while True:
        print("View attendance".center(60, "-"))
        view_input = input("""

present - Present students
absent  - Absent students
all     - All students
done    - When finished

Choice: """).strip().lower()

        if view_input == "present":
            print("\nList of Present Students")
            for index, present in enumerate(present_students, start=1):
                print(f"{index} - {present}")

        elif view_input == "absent":
            print("\nList of Absent Students")
            for index, absent in enumerate(absent_students, start=1):
                print(f"{index} - {absent}")

        elif view_input == "all":
            print("\nList of All Students")
            for index, student in enumerate(students, start=1):
                print(f"{index} - {student}")

        elif view_input == "done":
            break

        else:
            print("Choose one of the valid options.")


# Search student status
def search_student_status():
    clear()
    while True:
        search_input = input("Search student or type 'done' to exit: ").strip()

        if search_input.lower() == "done":
            break

        if search_input not in students:
            print("Student not in the list.")

        elif search_input in present_students:
            print(f"{search_input} is marked as Present.")

        elif search_input in absent_students:
            print(f"{search_input} is marked as Absent.")

# Download attendance
def download_attendance():
    filename = "attendance_report.txt"

    if students == [] and present_students == [] and absent_students == []:
        print("Student lists cannot be empty!")
        return

    with open(filename, "w") as file:
        file.write("Student Attendance Report\n")
        file.write("-" * 50 + "\n")

        file.write("Enrolled Students:\n")
        for i, s in enumerate(students, start=1):
            file.write(f"{i} - {s}\n")

        file.write("\nPresent Students:\n")
        for i, p in enumerate(present_students, start=1):
            file.write(f"{i} - {p}\n")

        file.write("\nAbsent Students:\n")
        for i, a in enumerate(absent_students, start=1):
            file.write(f"{i} - {a}\n")

    print(f"\nAttendance saved to '{filename}'")


# Main program
def main():
    clear()
    text_design()

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
            print("\nAttendance Checker")
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
                print("Choose one of the following options and try again!")

    except KeyboardInterrupt:
        print("\nAttendance checking cancelled.")


if __name__ == "__main__":
    main()
