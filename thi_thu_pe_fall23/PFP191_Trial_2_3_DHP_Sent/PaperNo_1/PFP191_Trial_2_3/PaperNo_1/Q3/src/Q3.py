# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class employees:
    def __init__(self,name,salary, age):
        self.name = name
        self.salary = salary
        self.age = age
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        n = int(input('Enter the number of employees: '))
        list = []
        for i in range (1,n+1):
            print(f'Employees {i}')
            name = input("Enter name: ")
            salary = input("Enter salary: ")
            age = input("Enter age: ")
            new_employees = employees(name,salary,age)
            list.append(new_employees)
        return list
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        for i in employeeList:
            
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        # end def




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


