#You can edit this function, if other function is neccessary, you can edit in this function
def Q3(lst, x):
    new_lst = []
    for i in lst:
        if i % x == 0:
            new_lst.append(i)
    return round(sum(new_lst) / len(new_lst), 2) 
#---------Do not edit this function---------
def main():
    n = int(input("Enter the number of element:"))
    lst = []
    for i in range(n):
        number = int(input("List:"))
        lst.append(number)
    x = int(input("Enter x = "))
    rs = Q3(lst, x)
    print(rs)


if __name__ == "__main__":
    main()