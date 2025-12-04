def text_design():
    print("-" * 48 + "\n" + "Student attendance checker".center(48, "-") + "\n" + "-" * 48)

# Lists of students
students = []
present_students = []
absent_students = []

def enroll_students():
    global students
    students = []

    print("\n Enroll Students ")
    print("Enter the student's name.")
    print("Type 'done' when finished. \n")

    while True:
        name = input("Enter student name: ").strip()

        if name.lower() == "done":
            break
        
        if name == "":
            print("Name cannot be empty.")
        elif name in students:
            print("Student already enrolled.")
        else:
            students.append(name)
            print(f"{name} added.")

    print("\nEnrollment complete.")
    print("Enrolled students:", students)

def record_attendance():
    global present_students, absent_students

    if not students:
        print("\n No students enrolled yet.")
        return
    
    present_students = []
    absent_students = []

    print("\n Record Attendance ")
    print("Enter the names of the Present students.")
    print("Type 'done' when finished.\n")

    while True:
        name = input("Present students.").strip()

        if name.lower() == 'done':
            break
         
        if name not in students:
            print("Students is not in the enrolled list.")
        elif name in present_students:
            print("This student is already marked present.")
        else:
            present_students.append(name)
            print(f"{name} is marked present.")

    absent_students = [s for s in students if s not in present_students]
    print("\n Attendance has been recorded.")

def download_attendance():
    filename = "attendance_report.txt"
    with open(filename, "w") as file:
        file.write("Student Attendance Report\n")
        file.write("---------------------------\n\n")

        file.write("Enrolled Students:\n")
        for s in students:
            file.write(f"- {s}\n")

        file.write("\nPresent Students:\n")
        for p in present_students:
            file.write(f"- {p}\n")

        file.write("\nAbsent Students:\n")
        for a in absent_students:
            file.write(f"- {a}\n")

    print(f"\nAttendance saved to '{filename}'")

# User had to choose their input
def main():
    text_design()
    while True:
        print("\n Attendance Checker")
        print("1. Enroll Students")
        print("2. Record Attendance")
        print("3. View Attendance Report")
        print("4. Search Student Status")
        print("5. Download Attendance File")
        print("6. Exit Program")
    
        choice = input("Choose an option 1-6: ")

        if choice == "1":
            enroll_students()

        elif choice == "2":
            record_attendance()

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            download_attendance()
        
        elif choice == "6":
            break

        else:
            pass

main()

