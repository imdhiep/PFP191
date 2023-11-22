# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Teacher:
    def __init__(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes
    def print_em(self):
        print(self.name)
        print(self.age)
        print(self.classes)
        
class Professor(Teacher):
    def __init__(self, name, age, classes, address):
        super().__init__(name, age, classes)
        self.address = address
    
    def display_info(self):
        print('Age:', self.age)
        print('Class:', self.classes)
        print('Name:', self.name)
        print('Address:', self.address)
        
        
    
    
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST TEACHERS========
    def InputListTeacher(self):
        n = input('Enter the number of teachers: ')
        n = int(n)
        teachers = []
        for i in range(n):
            print(f'Enter teacher {i + 1}')
            name = input('Enter name: ')
            age = input('Enter age: ')
            classes = input('Enter class: ')
            em = Teacher(name, age, classes)
            teachers.append(em)
        return teachers
        # end def
    def InputProfessor(self):
        pro = []
        name = input('Enter name: ')
        age = input('Enter age: ')
        classes = input('Enter class: ')
        address = input('Enter address: ')
        em = Professor(name, age, classes, address)
        pro.append(em)
        return pro
        # end def
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(len(teacherList)):
            print(f'Teacher {i + 1}')
            teacherList[i].print_em()
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        sorted_tea = sorted(teacherList, key = lambda emp: emp.age, reverse = True)
        for i in range(len(sorted_tea)):
            print(f'Teacher {i + 1}')
            sorted_tea[i].print_em()

        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================
        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        lst = [x for x in teacherList if x.classes[:2] == 'SE']
        sorted_tea = sorted(lst, key = lambda emp: emp.name)
        for i in range(len(sorted_tea)):
            print(f'Teacher {i + 1}')
            sorted_tea[i].print_em()
        # end def
    #==========================================

    # ====================f4====================
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        pro = self.InputProfessor()
        print("OUTPUT")
        # ==========================================
        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for x in pro:
            x.display_info()
       
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
