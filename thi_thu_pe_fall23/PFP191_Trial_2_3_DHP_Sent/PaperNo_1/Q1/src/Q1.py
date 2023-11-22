class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        a = inputString.split(',')
        for i in a:
            print(i.strip())
        pass
        # end def

    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        directions = inputString.split(", ")
        nums = []
        for d in directions:
            d = d.split(" ")
            if d[0] == "UP":
                nums.append(int(d[1])) 
            elif d[0] == "DOWN":
                nums.append(int(d[1]))
            elif d[0] == "LEFT":
                nums.append(int(d[1]))
            elif d[0] == "RIGHT":
                nums.append(int(d[1]))
        index = 0
        for i in nums:
            if index == 0:
                up = i
            if index == 1:
                down = i
            if index == 2:
                right = i
            if index == 3:
                left = i
            index += 1
            if index == 4:
                break
        a = 0
        b = 0
        a = a + int(up) - int(down)
        b = b + int(right) - int(left)
        location = (a**2+b**2)**0.5
        print(round(location))
    pass
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
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
