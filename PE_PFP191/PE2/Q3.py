# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST TEACHERS========
    def InputListTeacher(self):
        n = input('Enter the number of teachers: ')
        n = int(n)
        list = []
        for i in range(n):
            print(f"Enter teacher {i + 1}")
            print("Enter name: ", end='')
            name = input()
            print("Enter age: ", end='')
            age = int(input())
            print(f"Enter class: ", end='')
            clas = input()
            list.append([name, age, clas])
        return list
        # end def
    def InputProfessor(self):
        list = []
        print("Enter name: ", end='')
        name = input()
        list.append(name)
        
        print("Enter age: ", end='')
        age = int(input())
        list.append(age)
        
        print("Enter class: ", end='')
        clas = input()
        list.append(clas)
        
        print("Enter address: ", end='')
        add = input()
        list.append(add)
        return list

        # end def
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list = teacherList
        for i in range(len(list)):
            print(f"Teacher {i + 1}")
            for j in list[i]:
                print(j)
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list = teacherList.copy()
        list.sort(key= lambda x: x[1], reverse= True)
        for i in range(len(list)):
            print(f"Teacher {i + 1}")
            for j in list[i]:
                print(j)
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list = teacherList.copy()
        for i in teacherList:
            if i[2][:2] != "SE":
                list.remove(i)
        list.sort(key= lambda x: x[0])
        for i in range(len(list)):
            print(f"Teacher {i + 1}")
            for j in list[i]:
                print(j)
        # end def
    #==========================================

    # ====================f4====================
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        pro = self.InputProfessor()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        print("Age: ", end='')
        print(pro[1])
        print("Class: ", end='')
        print(pro[2])
        print("Name: ", end='')
        print(pro[0])
        print("Address: ", end='')
        print(pro[3])
            
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
