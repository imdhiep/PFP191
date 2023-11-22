# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        n = input('Enter the number of student: ')
        n = int(n)
        list = []
        for i in range(n):
            print(f"Enter employees {i + 1}")
            print("Enter name: ", end='')
            name = input()
            print("Enter salary: ", end='')
            salary = int(input())
            print(f"Enter age: ", end='')
            age = input()
            list.append([name, salary, age])
        return list
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        #Print Employee List
        list = employeeList
        for i in range(len(list)):
            print(f"Employee {i + 1}")
            for j in list[i]:
                print(j)
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list = employeeList.copy()
        list.sort(key= lambda x: x[1], reverse= True)
        for i in range(len(list)):
            print(f"Employee {i + 1}")
            for j in list[i]:
                print(j)
    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
         #Print Employee List after sorted
        list = []
        for employee in employeeList:
            age = int(employee[2])
            if age >= 18:
                list.append(employee)
        list.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(list)):
            print(f"Employee {i + 1}")
            for j in list[i]:
                print(j)
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
