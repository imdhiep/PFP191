# Q1
# def find_min(a, b, c):
#     return min(a, b, c)
# 
# # Assuming the existing code to input a, b, c is here
# # a = ...
# # b = ...
# # c = ...
# 
# min_value = find_min(a, b, c)
# print(min_value)
# Q2
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# 
# def find_prime_sum(m):
#     return sum(i for i in range(2, m) if is_prime(i))
# 
# # Assuming the existing code to input m is here
# # m = ...
# # m = int(input("Nhap m: "))
# prime_sum = find_prime_sum(m)
# print(prime_sum)
# Q3
# def average_divisible_by_x(lst, x):
#     # List comprehension to get elements divisible by x
#     divisible_elements = [i for i in lst if i % x == 0]
# 
#     # Calculate the average
#     if divisible_elements:
#         avg = sum(divisible_elements) / len(divisible_elements)
#         return round(avg, 2)
#     else:
#         return 0.0  # Return 0 if no elements are divisible by x
# 
# # Assuming the existing code to input the list and x is here
# # number_of_elements = int(input("Enter the number of elements: "))
# # lst = [int(input()) for _ in range(number_of_elements)]
# # x = int(input("Enter x = "))
# 
# average = average_divisible_by_x(lst, x)
# print(f"{average:.2f}")
# Q4
# def sum_digits_in_string(s):
#     return sum(int(c) for c in s if c.isdigit())
# 
# # Assuming the existing code to input str is here
# str = input("Enter a string: ")
# 
# sum_digits = sum_digits_in_string(str)
# print(sum_digits)


