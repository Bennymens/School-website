import json

# File paths for storing data
STUDENTS_FILE = "students.json"
TEACHERS_FILE = "teachers.json"

# Load data from files
def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file does not exist

# Save data to files
def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file)

# Load initial data
students = load_data(STUDENTS_FILE)
teachers = load_data(TEACHERS_FILE)

# Function to regisr a new student
def register_student(student_id, student_name):
    if student_id in students:
        print("Student ID already exists. Please use a different ID.")
    else:
        password = input("Set a password: ")
        students[student_id] = {"name": student_name, "password": password}
        save_data(STUDENTS_FILE, students)  # Save updated students data
        print(f"Student {student_name} with ID {student_id} registered successfully.")

# Function to log in a student
def student_login(student_id):
    if student_id in students:
        password = input("Enter your password: ")
        if password == students[student_id]["password"]:
            print(f"Welcome, {students[student_id]['name']}!")
        else:
            print("Error: Incorrect password.")
    else:
        print("Error: Student ID not found. Please try again.")

# Function to register a new teacher
def register_teacher(teacher_id, teacher_name):
    if teacher_id in teachers:
        print("Teacher ID already exists. Please use a different ID.")
    else:
        password = input("Set a password: ")
        teachers[teacher_id] = {"name": teacher_name, "password": password}
        save_data(TEACHERS_FILE, teachers)  # Save updated teachers data
        print(f"Teacher {teacher_name} with ID {teacher_id} registered successfully.")

# Function to log in a teacher
def teacher_login(teacher_id):
    if teacher_id in teachers:
        password = input("Enter your password: ")
        if password == teachers[teacher_id]["password"]:
            print(f"Welcome, {teachers[teacher_id]['name']}!")
        else:
            print("Error: Incorrect password.")
    else:
        print("Error: Teacher ID not found. Please try again.")

# Main program
while True:
    print("\n--- School App ---")
    print("1. Register Student")
    print("2. Student Login")
    print("3. Register Teacher")
    print("4. Teacher Login")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        register_student(student_id, student_name)
    elif choice == "2":
        student_id = input("Enter Student ID to log in: ")
        student_login(student_id)
    elif choice == "3":
        teacher_id = input("Enter Teacher ID: ")
        teacher_name = input("Enter Teacher Name: ")
        register_teacher(teacher_id, teacher_name)
    elif choice == "4":
        teacher_id = input("Enter Teacher ID to log in: ")
        teacher_login(teacher_id)
    elif choice == "5":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
