# #Q1
# 
# def find_min(a, b, c):
#     """Finds the minimum of three numbers."""
#     min_value = a  
#     if b < min_value:
#         min_value = b
#     if c < min_value:
#         min_value = c
#     return min_value
# 
# if __name__ == "__main__":
#     a = 3 
#     b = 7
#     c = 6
#     min_value = find_min(a, b, c)
#     print(min_value)
# 
# #Q2 
# 
# def is_prime(n):
#     """Returns True if n is a prime number, False otherwise."""
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# 
# def sum_of_primes(n):
#     """Returns the sum of the primes less than n."""
#     sum_of_primes = 2
#     for i in range(3, n):
#         if is_prime(i):
#             sum_of_primes += i
#     return sum_of_primes
# 
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     sum_of_primes = sum_of_primes(n) 
#     print("The sum of the primes less than {} is {}".format(n, sum_of_primes))
# 
# #Q3
# def find_average(list_of_numbers, x):
#     """Tính trung bình cộng của các phần tử chia hết cho x trong danh sách"""
#     sum_of_divisible_elements = 0
#     number_of_divisible_elements = 0
# 
#     for element in list_of_numbers:
#         if element % x == 0:
#             sum_of_divisible_elements += element
#             number_of_divisible_elements += 1
#     
#     if number_of_divisible_elements == 0:
#         return 0
#     else:
#         return round(sum_of_divisible_elements / number_of_divisible_elements, 2)
# 
# if __name__ == "__main__":
#     number_of_elements = int(input("Nhập số phần tử: "))
#     list_of_numbers = list(map(int, input("Danh sách: ").split())) 
#     x = int(input("Nhập x = "))
#     
#     average = find_average(list_of_numbers, x)
#     print(format(average))

#Q4
def sum_of_digits(str):
   """Tính tổng các chữ số trong chuỗi"""
   sum_of_digits = 0
   
   for character in str:
       if character.isdigit():
           sum_of_digits += int(character)
           
   return sum_of_digits

if __name__ == "__main__":
   str = input("Nhập vào một chuỗi: ") 
   sum_of_digits = sum_of_digits(str)  
   
   print("Tổng các chữ số = {} ".format(sum_of_digits))