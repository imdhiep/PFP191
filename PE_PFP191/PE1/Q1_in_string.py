class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if re.search("[a-z]", i) and 'c' not in i:
                print(i)
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if re.search("[1,3,5,7,9]", i):
                print(i)        
        # end def
        
    #====================f2====================
    def f3(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if re.search("[A-Z]", i):
                print(i)        
        # end def
        
    #====================f2====================
    def f4(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if re.search("[$,#,@,&]", i):
                print(i)        
        # end def

    def f5(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if len(i) >= 6:
                print(i)        
        # end def
        
    def f6(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if len(i) <= 12:
                print(i)        
        # end def
        
    def f7(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        list = inputString.split(',')
        for i in list:
            if (re.search("[a-z]", i) and ('c' not in i)) and (re.search("[A-Z]", i)) and (re.search("[1,3,5,7,9]", i)) and (re.search("[$,#,@,&]", i)) and (len(i) >= 6) and (len(i) <= 12):
                print(i)        
        # end def
#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        elif choice == 3:
            self.f3(inputString)
        elif choice == 4:
            self.f4(inputString)
        elif choice == 5:
            self.f5(inputString)
        elif choice == 6:
            self.f6(inputString)
        elif choice == 7:
            self.f7(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

