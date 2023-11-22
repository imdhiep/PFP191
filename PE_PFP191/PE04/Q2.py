class Main:
    #====================f1====================
    def f1(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # end def
        

    #====================f2====================
    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # end def
    
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        print("OUTPUT")
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()