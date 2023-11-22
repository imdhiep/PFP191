class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        pos = [0,0]
        while True:
            s = input("Enter Steps: ")
            if not s:
                break
            movement = s.split(" ")
            direction = movement[0].upper()
            steps = int(movement[1])
            if direction=="UP":
                pos[0]+=steps
            elif direction=="DOWN":
                pos[0]-=steps
            elif direction=="LEFT":
                pos[1]-=steps
            elif direction=="RIGHT":
                pos[1]+=steps
            distance = (pos[1]**2 + pos[0]**2)**0.5
            print(int(round(distance)))


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
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
