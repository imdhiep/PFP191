# Câu 1:
#  Input information
x = input(" What is your name : ")
y = input(" what is your ID : ")
z = input(" which class are you in : ")
#  Print information
print("Name :" , x)
print("ID:", y)

# Câu 2
#input Celsius
celsius = float(input("Enter temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# Output in Fahrenheit
print("Temperature in Fahrenheit: ", fahrenheit)

# Câu 3
# Input dog's age
dog_age = float(input("Enter the dog's age in years: "))
# Calculate human age
if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = 21 + (dog_age - 2) * 4
# Output the human age
print("The dog's age in human years is:", human_age)

# Câu 4
# Print the list of months
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# Input the name of the month
month = input("Enter the name of the month: ")
# Check the name of the month and assign the number of days accordingly
if month == "February":
    days = "28 or 29" # Assume a non-leap year
elif month in ["April", "June", "September", "November"]:
    days = 30
else:
    days = 31
# Print the number of days in the month
print(f"The number of days in {month} is {days}.")

# Câu 5
# Yêu cầu người dùng nhập độ dài các cạnh của tam giác
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác này là tam giác đều.")
    elif a == b or b == c or a == c:
        print("Tam giác này là tam giác cân.")
    else:
        print("Tam giác này là tam giác thường.")
else:
    print("Ba cạnh này không tạo thành một tam giác.")

# Câu 7 
# Yêu cầu người dùng nhập ngày, tháng, năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra ngày hợp lệ
if ngay < 1 or ngay > 31 or thang < 1 or thang > 12 or nam < 1:
    print("Ngày không hợp lệ.")
else:
    print("Ngày hợp lệ.")
