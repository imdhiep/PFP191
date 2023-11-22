def checkTriangle(a,b,c):
    result = 0
    #Begin your statements here
    if a + b > c and b + c > a and c + a > b:
           result = 1
    #End your statements
    return result
#end checkTriangle
#-----------------------------------------------------------------------------
#=============DO NOT ADD NEW OR CHANGE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("Test Q1 (2 marks)")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    result = checkTriangle(a, b, c)
    print("OUTPUT:")
    print(result)
#end main
#=================DO NOT ADD NEW OR CHANGE THIS STATEMENTS =====================
if __name__ == '__main__':
    main()
