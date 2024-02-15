"""
1.wap to take 10 students details from terminal (name,age,religion)
make a dictionary for every students and push all items to a list of students 
transform list of students dict to list of dict with names only
filter list of students of age 20
"""

students = []

for i in range(5):
    name = input("Enter student's name: ")

    while True:
        try:
            age = int(input("Enter student's age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    religion = input("Enter student's religion: ")
    student = {"name": name, "age": age, "religion": religion}
    students.append(student)

# Transform list of students dict to list of dict with names only
student_names = [student["name"] for student in students]


# Filter list of students of age 20
students_age_20 = [student for student in students if student["age"] == 20]
print("Student names: ", student_names)
print("Students of age 20: ", students_age_20)
