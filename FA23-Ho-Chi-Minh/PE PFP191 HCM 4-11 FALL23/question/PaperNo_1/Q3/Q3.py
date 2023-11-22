#--------------------------
def count(li:list):
    # Write your statements here
    return None
    # End your statements
#end count
# DO NOT ADD NEW OR CHANGE STATEMENTS IN THIS FUNCTION
def inputList(li, n):
    for i in range(n):
        li.append(int(input(f"Element[{i}]=")))
# end inputList
#=====================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.=======================
def main():
  print("TEST Q3 (2 marks):");
  li = list()
  n = int(input("Enter number of elements : "))
  inputList(li, n)
  print("OUTPUT:")
  e = count(li)
  print(f"{e}")
#end main
#------------------------------------
if __name__ == "__main__":
  main()
#============================================================================================
