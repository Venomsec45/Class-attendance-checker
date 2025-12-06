def text_design():
    print("-" * 48 + "\n" + "Student attendance checker".center(48, "-") + "\n" + "-" * 48)

# Lists of students
students = []
present_students = []
absent_students = []

# Enroll students
def enroll_students():
    global students
    students = []

    print("\n Enroll Students ")
    print("Enter the student's name.")
    print("Type 'done' when finished. \n")

    while True:
        name = input("Enter student name or type 'done' to exit: ").strip()

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

# Record attendance
def record_attendance():
    global present_students, absent_students

    if not students:
        print("\nNo students enrolled yet.")
        return
    
    present_students = []
    absent_students = []

    print("\nRecord Attendance ")
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

def view_attendance():
    while True:
        view_input = input("""View attendance

Present - Present students
Absent - Absent students
All - All students
            
Choice: """).strip()
        
        if view_input == "Present":
            print("List of present students")
            for index, present in enumerate(present_students, start=1):
                print(f"{index} - {present}")
            break

        elif view_input == "Absent":
            print("List of absent students")
            for index, absent in enumerate(absent_students, start=1):
                print(f"{index} - {absent}")
            break

        elif view_input == "All":
            print("List of all students")
            for index, all in enumerate(students, start=1):
                print(f"{index} - {all}")
            break
        
        else:
            print("Choose one of the following options and try again!")

def search_student_status():
    while True:
        search_input = input("Search student or type 'done' to exit: ")

        if search_input == "done":
            break

        elif search_input not in students:
            print("Student not in the list")
        
        elif search_input in present_students:
            print(f"{search_input} marked as present")
        
        elif search_input in absent_students:
            print(f"{search_input} marked as absent")

        else:
            pass

def download_attendance():
    filename = "attendance_report.txt"
    with open(filename, "w") as file:
        file.write("Student Attendance Report\n")
        file.write("---------------------------\n\n")

        file.write("Enrolled Students:\n")
        for s in students:
            file.write(f" - {s}\n")

        file.write("\nPresent Students:\n")
        for p in present_students:
            file.write(f" - {p}\n")

        file.write("\nAbsent Students:\n")
        for a in absent_students:
            file.write(f" - {a}\n")

    print(f"\nAttendance saved to '{filename}'")

# User had to choose their input
def main():
    text_design()
    choices = {"1": enroll_students,
               "2": record_attendance,
               "3": view_attendance,
               "4": search_student_status,
               "5": download_attendance,
               "6": exit}
    try:
        while True:
            print("\nAttendance Checker")
            print("1. Enroll Students")
            print("2. Record Attendance")
            print("3. View Attendance Report")
            print("4. Search Student Status")
            print("5. Download Attendance File")
            print("6. Exit Program")
        
            choice = input("\nChoose an option (1-6): ")
            if choice in choices:
                choices[choice]()
            
            print("Choose one of the following options and try again!")
    
    except KeyboardInterrupt:
        print("\nAttendance checking cancelled")

if __name__ == "__main__":
    main()


            # if choice == "1":
            #     enroll_students()

            # elif choice == "2":
            #     record_attendance()

            # elif choice == "3":
            #     view_attendance()

            # elif choice == "4":
            #    search_student_status()

            # elif choice == "5":
            #     download_attendance()
            
            # elif choice == "6":
            #     print("Exiting attendance checker")
            #     break

            # else:
            #     print("Choose among the choices and try again!")
