# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST TEACHERS========
    def InputListTeacher(self):
        n = input('Enter the number of teachers: ')
        x = 1
        l1 =[]
        while x <= int(n) :
            d1 = dict()
            print(f"Enter teacher {x}")
            na = input("Enter name: ")
            ag = input("Enter age: ")
            cla = input("Enter class: ")
            d1['name'] = na
            d1['age'] = ag
            d1['class'] = cla
            l1.append(d1)
            x +=1
        return l1
        # end def
    def InputProfessor(self):
        
        return
        # end def
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        x =1
        for i in teacherList:
            print(f'Teacher {x}')
            x+=1
            for val in i.values():
                print(val) 
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        teacherList.sort(key = lambda x: x['age'], reverse=True)
        x=1
        for i in teacherList:
            print(f'Teacher {x}')
            x+=1
            for val in i.values():
                print(val)
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        x=1
        for i in teacherList:
            l1 = i["name"].split(" ")
            l1.sort(lambda y: y[l1[-1]])
            if "SE" in i["class"]:
                print(f'Teacher {x}')
                x+=1
                for val in i.values():
                    print(val)
        # end def
    #==========================================

    # ====================f4====================
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        pro = self.InputProfessor()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
       
        # end def    
    # ==========================================


#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" 4. Test f4 (1 mark)")
        print(" Your selection (1 -> 4): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        elif choice == 4:
            self.f4()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
