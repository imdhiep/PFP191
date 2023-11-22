class Main:
    #====================f1====================
    def f1(self, inputWidth, inputHeight):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        w = inputWidth
        h = inputHeight
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or j == w-1 or i == h-1:
                    print("*", end='')
                    continue
                print(" ", end='')
            print('')
        pass

        # end def
    
    #====================f1====================
    def f2(self, inputWidth, inputHeight):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        w = inputWidth
        h = inputHeight
        for i in range(h):
            for j in range(w + h - 1):
                if (i == 0 and j >= h-1) or (i == h-1 and j <= w-1) or j == h-i-1 or j == w+h-i-2:
                    print("*", end='')
                    continue
                if j <= w+h-i-2:
                    print(" ", end='')
            print('')                    
        pass
        
        # end def


    #====================f2====================
    def f3(self, inputWidth, inputHeight):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        w = inputWidth
        h = inputHeight
        for i in range(h):
            for j in range(w):
                print("*", end='')
            print('')
        pass

        # end def
        
    #====================f2====================
    def f4(self, inputWidth, inputHeight):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        w = inputWidth
        h = inputHeight
        for i in range(h):
            for j in range(w+h):
                if j >= i and j <= w+i:
                    print("*", end='')
                elif j <= w+i:
                    print(" ", end='')
            print('')        
        pass
    
        # end def
    #====================f2====================
    def f5(self, inputWidth, inputHeight):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        w = inputWidth
        h = inputHeight
        for i in range(h):
            for j in range(w+h):
                if j >= h-i-1 and j <= w+h-i-2:
                    print("*", end='')
                elif j <= w+h-i-2:
                    print(" ", end='')
            print('')            
        pass
    
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (0.5 mark)")
        print(" 2. Test f2 (0.5 mark)")
        print(" 3. Test f3 (0.5 mark)")
        print(" 4. Test f4 (0.5 mark)")
        print(" 5. Test f5 (1.0 mark)")
        print(" Your selection (1 -> 5): ")
        choice = int(input())
        inputWidth = int(input('Please enter the width of the parallelogram: '))
        inputHeight = int(input('Please enter the height of the parallelogram: '))
        print("OUTPUT")
        if choice == 1:
            self.f1(inputWidth, inputHeight)
        elif choice == 2:
            self.f2(inputWidth, inputHeight)
        elif choice == 3:
            self.f3(inputWidth, inputHeight)
        elif choice == 4:
            self.f4(inputWidth, inputHeight)
        elif choice == 5:
            self.f5(inputWidth, inputHeight)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()


