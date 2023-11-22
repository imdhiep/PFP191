class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        file = open(fileName, 'r')
        content = file.read()
        print(content)
        pass
        
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        file = open(fileName, 'r')
        content = file.read().split(', ')
        d = 0
        w = 0
        for i in range(len(content)):
            if content[i][0] == 'D':
                d += int(content[i][2:])
            if content[i][0] == 'W':
                w += int(content[i][2:])
                
        print(d - w)
        
        pass


        
        # end def
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        fileName = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(fileName)
        elif choice == 2:
            self.f2(fileName)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
