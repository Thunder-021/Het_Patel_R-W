

print("\n\ Welcome to the Student Data Organizer! ")
print("This program helps manage student records using Python collections.")
print("---------------------------------------------------------------\n")


students = []

subjects_offered = set()



def add_student():
    print("\n--- Add New Student ---")

    try:
        student_id = int(input("Student ID: "))  # type casting
    except ValueError:
        print("Invalid ID! Must be a number.")
        return

    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")

    identity = (student_id, dob)

    subjects = set(s.strip() for s in input("Subjects (comma-separated): ").split(","))

    subjects_offered.update(subjects)

    student_dict = {
        "id_and_dob": identity,  
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": list(subjects)  
    }

    students.append(student_dict)

    print("\nStudent added successfully!\n")


def display_students():
    print("\n--- Displaying All Students ---")

    if not students:
        print("No student records available.\n")
        return

    for student in students:
        sid, dob = student["id_and_dob"]

        print(f"\nStudent ID: {sid} | Name: {student['name']} | "
              f"Age: {student['age']} | Grade: {student['grade']}")

        print("Subjects: {}".format(", ".join(student["subjects"])))

        print("DOB (stored in tuple): %s" % dob)

    print()  


def update_student():
    print("\n--- Update Student Information ---")

    try:
        sid = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Invalid ID! Must be a number.")
        return

    for student in students:
        if student["id_and_dob"][0] == sid:
            print("\nWhat would you like to update?")
            print("1. Age")
            print("2. Grade")
            print("3. Subjects")
            choice = input("Enter choice: ")

            if choice == "1":
                new_age = int(input("Enter new age: "))
                student["age"] = new_age  
                print("Age updated!")

            elif choice == "2":
                new_grade = input("Enter new grade: ")
                student["grade"] = new_grade
                print("Grade updated!")

            elif choice == "3":
                new_subjects = set(s.strip() for s in input("New subjects: ").split(","))
                student["subjects"] = list(new_subjects)
                subjects_offered.update(new_subjects)
                print("Subjects updated!")

            else:
                print("Invalid choice.")

            return

    print("Student ID not found.\n")



def delete_student():
    print("\n--- Delete Student ---")
    try:
        sid = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("ID must be a number!")
        return

    for i, student in enumerate(students):
        if student["id_and_dob"][0] == sid:
            del students[i]  # DEL KEYWORD
            print("Student record deleted successfully!\n")
            return

    print("Student not found.\n")



def display_subjects():
    print("\n--- Subjects Offered ---")
    if not subjects_offered:
        print("No subjects added yet.")
    else:
        for s in subjects_offered:
            print("-", s)
    print()



while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break
    else:
        print("Invalid option. Please try again.\n")
