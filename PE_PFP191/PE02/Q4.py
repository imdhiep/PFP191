#You can edit this function, if other function is neccessary, you can edit in this function
def Q4(string):
    lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total = 0
    for text in string:
        if text in lst:
            total += int(text)
    return total
#---------Do not edit this function---------
def main():
    string = input("Input:")
    rs = Q4(string)
    print("After processing:", rs)

if __name__ == "__main__":
    main()