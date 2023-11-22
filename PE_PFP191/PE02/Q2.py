#You can edit this function, if other function is neccessary, you can edit in this function
def check_prime(number):
    cnt = 0
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    return False

def Q2(n):
    total = 0
    for number in range(1, n):
        if check_prime(number):
            total +=  number
    return total
#---------Do not edit this function---------
def main():
    n = int(input("Enter the number:"))
    rs = Q2(n)
    print(rs)


if __name__ == "__main__":
    main()