class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        data = open(fileName, 'r')
        content = data.read().split()
        for i in content:
            print(i)

        pass
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        data = open(fileName, 'r')
        content = data.read().split()
        for number in content:
            number = int(number)
            s = str(number) + ' = '
            i = 2
            while i*i <= number:
                if number % i == 0:
                    s += str(i) + ' x '
                    number = number // i
                else:
                    i += 1 
            s += str(number)
            print(s)
        pass
        # end def
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
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
