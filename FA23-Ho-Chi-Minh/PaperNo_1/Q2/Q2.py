def is_prime(n):
   if n <= 1:
       return False
   if n <= 3:
       return True
   if n % 2 == 0 or n % 3 == 0:
       return False
   i = 5
   while i * i <= n:
       if n % i == 0 or n % (i + 2) == 0:
           return False
       i += 6
   return True
def find_primes(x, y):
   primes = []
   for num in range(min(x, y), max(x, y) + 1):
       if is_prime(num):
           primes.append(num)
   return primes
def averageAllPrimes(x, y):
   primes = find_primes(x, y)
   if not primes:
       return 0
   return sum(primes) / len(primes)
#-----------------------------------------------------------------------------
#=============DO NOT ADD NEW OR CHANGE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("Test Q2 (3 marks)")
    x = int(input("x = "))
    y = int(input("y = "))
    print("OUTPUT:")
    result = averageAllPrimes(x, y)
    print(f"{result:.2f}")
#end main
if __name__ == '__main__':
    main()
