#You can edit this function, if other function is neccessary, you can edit in this function
def Q1(a, b, c):
    if a > b:
        if b > c:
            return c
        else:
            return b
    else:
        if a < c:
            return a
        else:
            return c

#---------Do not edit this function---------
def main():
    a = int(input("Enter the number 1:"))
    b = int(input("Enter the number 2:"))
    c = int(input("Enter the number 3:"))
    rs = Q1(a, b, c)
    print(rs)


if __name__ == "__main__":
    main()
