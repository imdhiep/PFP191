class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list_s = inputString.split(", ")
        for s in list_s:
            print(s)
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list_s = inputString.split(", ")
        dict_s = dict()
        for s in list_s:
            s_item = s.split(" ")
            dict_s[s_item[0]] = s_item[1]
        robot_pos = [0,0]
        for itemp in dict_s.items():
            item = list(itemp)
            item[0] = str(item[0])
            item[1] = int(item[1])
            if item[0] == "UP":
                robot_pos[1] += item[1]
            if item[0] == "DOWN":
                robot_pos[1] -= item[1]
            if item[0] == "LEFT":
                robot_pos[0] -= item[1]
            if item[0] == "RIGHT":
                robot_pos[0] += item[1]
        distance = (robot_pos[0]**2+robot_pos[1]**2)**0.5
        print(round(distance))
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
