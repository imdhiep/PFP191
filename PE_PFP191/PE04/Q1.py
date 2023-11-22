class Main:
#====================f1====================
    def f1(self, x, y): #check valid password
# ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

# end def


    def f2(self, x, y): #check valid password
# ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
# end def
    #================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        x = int(input("Enter number of row:"))
        y = int(input("Enter number of col:"))
        
        print("OUTPUT")
        if choice == 1:
            answer1 = self.f1(x, y)
            print("Matrix:")
            print(answer1)
        elif choice == 2:
            sum_follow_col, sum_follow_row = self.f2(x, y)
            print("Total follow col:", sum_follow_col)
            print("Total follow row:", sum_follow_row)
        print("FINISH")
    
main = Main()
main.main()