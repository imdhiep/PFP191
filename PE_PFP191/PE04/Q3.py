class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getall(self):
        print(self.x)
        print(self.y)        
    
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputPointList(self):
        list_point = []
        n = int(input('Enter the number of point: '))
        for i in range(n):
            print(f"Enter point {i+1}")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            b = point(x, y)
            list_point.append(b)
        return list_point    

        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        pointList = self.InputPointList()
        x0, y0 = 1, 2
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
      
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        pointList = self.InputPointList()
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        pointList = self.InputPointList()
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # end def
    #==========================================




#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()