"""
1.wap to take 10 students details from terminal (name,age,religion)
make a dictionary for every students and push all items to a list of students 
transform list of students dict to list of dict with names only
filter list of students of age 20
"""


def take_student_details():
    students = []
    for i in range(3):
        name = input("Enter name of student {}: ".format(i + 1))
        age = int(input("Enter age of student {}: ".format(i + 1)))
        religion = input("Enter religion of student {}: ".format(i + 1))
        student = {"name": name, "age": age, "religion": religion}
        students.append(student)
    return students


def transform_students_list(students):
    transformed_students = [{"name": student["name"]} for student in students]
    return transformed_students


def filter_students_by_age(students, age):
    filtered_students = [student for student in students if student["age"] == age]
    return filtered_students


students = take_student_details()
transformed_students = transform_students_list(students)
filtered_students = filter_students_by_age(transformed_students, 20)

for student in transformed_students:
    print("Name: {}".format(student["name"]))
    print("\n")

print("Students of age 20:")
for student in filtered_students:
    print("Name: {}".format(student["name"]))
    print("\n")
