# #De 2 - Cau 1
# # ta sẽ sử dụng hàm hàm randint trong thư viện random để tạo một số tự nhiên ngẫu nhiên trong đoạn start,end
# # format:      random.randint(start, end)   hoặc trong trường hợp này       randint(start, end)
# from random import randint
# start = 0 
# 
# 
# # Lấy phần end là một số nguyên từ người dùng, nếu sai input --> báo lỗi
# try:
#     end = int(input('Enter a range for the guessed number: '))
# except:
#     print('Error')
# 
# # chạy vòng lặp cho đến khi máy đoán đúng
# while True:
#     # máy tạo một số nguyên ngẫu nhiên trong đoạn start, end
#     computer_guess = randint(start, end)
# 
#     # lấy thông tin từ người dùng xem số của máy lớn hơn, nhỏ hơn hay bằng số của máy
#     guess = input((f'Is {computer_guess} too high(h), too low(l), or correct(c): '))
# 
#     if guess == 'l':    # Nếu số của máy bé hơn thì cập nhật biến start
#         start = computer_guess + 1
#     
#     elif guess == 'h':  # Nếu số của máy bé hơn thì cập nhật biến end
#         end = computer_guess - 1
# 
#     elif guess == 'c': # Nếu số của máy bé đúng thì in ra
#         print(f'Welldone! The computer guessed your number {computer_guess} correctly!')
#         break

#De 2 - Cau 1
path = 'D:/Code/Ki 1/Training/PE Prepare'
# nhập tên file
file_name = input('Enter a file name: ')

# Đọc dữ liệu từ file
f =  open(path+file_name, 'r')
data = f.readlines() #đọc từng dòng dữ liệu trong file

# có thể thấy có kí tự \n báo hiệu xuống dòng, ta cần loại bỏ kí tự thừa này
for i in range(len(data)):
    data[i] = data[i].replace('\n', '') # xoá '\n' khi đọc file

req = [] # dùng để lưu trữ yêu cầu (request)
amount = [] # dùng để lưuu trữ số lượng
# index của request ở req sẽ tương ứng với số lượng ở amount
for i in data:
    req.append(i.split()[0])
    amount.append(int(i.split()[1])) # nhớ ép kiểu int cho số vì lúc nhập vào nó sẽ ở dạng string

# Tính toán
balance = 0 
for i in range(len(req)):
    if req[i] == 'D':
        balance += amount[i] # balance = balance + amount[i]
    elif req[i] == 'W':
        balance -= amount[i]

# In ra theo yêu cầu
while True: # vòng lặp sẽ lặp đi lặp lại cho đến khi input vào option là 2
    option = int(input('Enter an option (1. Content - 2. Compute): '))
    if option == 1:
        print("Content:", ', '.join(data))
    elif option == 2:
        print(balance)
        break

#De 2 - Cau 3
class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

def sort_key(Student):
    return Student.name

students = []

while True:     # kiểm tra xem input có đúng là một số không
    number_of_students = input("Enter the number of students: ")
    if number_of_students.isdigit():
        break
    else:
        print("Please enter a number!")

# nhập thông tin từng học sinh
for i in range(int(number_of_students)):
    temp = int(input("Enter student :")) 
    students.append(Student(
                input('Enter name: '),
                int(input('Enter age: ')),
                int(input('Enter mark: '))
                ))
 
print("Before softing")     
for i in range(len(students)):      # in danh sách trước khi sắp xếp
    print("Student ", i + 1)
    print("Name : {}\nMark : {}\nAge : {}".format(students[i].name, students[i].mark, students[i].age))

print("After softing")


students.sort(key=sort_key, reverse=False)      # sắp xếp
# key=func, hàm sẽ sắp xếp các phần tử trong list theo giá trị trả về của key, trong trường hợp này là name

for i in range(len(students)):      # in danh sách sau khi sắp xếp
    print("Student ", i + 1)
    print("Name : {}\nMark : {}\nAge : {}".format(students[i].name, students[i].mark, students[i].age))
