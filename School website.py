# Predefined list of valid student IDs and names
students = {
    "12345": "John Doe",
    "67890": "Jane Smith",
    "11223": "Alice Brown"
}

# Function to register a new student
def register_student(student_id, student_name):
    if student_id in students:
        print("Student ID already exists. Please use a different ID.")
    else:
        students[student_id] = student_name
        print(f"Student {student_name} with ID {student_id} registered successfully.")

# Input from the user
student_id = input("Enter your ID: ")
student_name = input("Enter your name: ")

# Check if the student ID is valid
if student_id in students and students[student_id] == student_name:
    print(f"Welcome, {student_name}!")
else:
    print("Access denied. Invalid ID or name.")

