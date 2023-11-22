class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    
number_student = input("Enter the number of students:")
while True:
    try:
        number_student = int(number_student)
        break
    except:
        number_student = input("Enter the number of students:")

lst_student = []
for student_id in range(number_student):
    print(f"Enter student: {student_id+1}")
    name = input("Enter name:")
    age = input("Enter age:")
    while True:
        try:
            age = int(age)
            break
        except:
            age = input("Enter age:")
    while age < 0:
        age = input("Enter age:")
        while True:
            try:
                age = int(age)
                break
            except:
                age = input("Enter age:")

    mark = float(input("Enter mark:"))
    while True:
        try:
            mark = float(mark)
            break
        except:
            mark = input("Enter mark:")
    while mark < 0 or mark > 10:
        mark = input("Enter mark:")
        while True:
            try:
                mark = float(mark)
                break
            except:
                mark = input("Enter mark:")

    student = Student(name, age, mark)
    lst_student.append(student)

print("Before sorting:")
for i, obj in enumerate(lst_student):
    print(f"Student: {i+1}")
    print(f"Name: {obj.name}")
    print(f"Mark: {obj.mark}")
    print(f"Age: {obj.age}")
new_lst_student = sorted(lst_student, key=lambda x: x.name)

print("After sorting:")
for i, obj in enumerate(new_lst_student):
    print(f"Student: {i+1}")
    print(f"Name: {obj.name}")
    print(f"Mark: {obj.mark}")
    print(f"Age: {obj.age}")