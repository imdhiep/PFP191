# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputListBook(self):
        n = input('Enter the number of books: ')
        list = []
        for i in range(int(n)):
            print(f"Enter book {i + 1}")
            print("Enter name : ", end='')
            name = input()
            print("Enter year : ", end='')
            year = input()
            print("Enter doi : ", end='')
            doi = input()
            list.append([name, year, doi])            
        return list
        # end def
    def InputNovel(self):
        list = []
        print("Enter name : ", end='')
        name = input()
        print("Enter year : ", end='')
        year = input()
        print("Enter doi : ", end='')
        doi = input()
        print("Enter author : ", end='')
        author = input()
        list.append(year)
        list.append(doi)
        list.append(name)
        list.append(author)
        return list
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(len(bookList)):
            print("Book", i + 1)
            print(bookList[i][0])
            print(bookList[i][1])
            print(bookList[i][2])            
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(len(bookList)):
            print("Book", i + 1)
            print(bookList[i][0])
            print(bookList[i][1])
            print(bookList[i][2])            
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        list = bookList.copy()
        for i in bookList:
            if i[2][:7] != '10.1000':
                list.remove(i)
           
        list = sorted(list, key= lambda x: x[1], reverse= True)
        for i in range(len(list)):
            print("Book", i + 1)
            print(list[i][0])
            print(list[i][1])
            print(list[i][2])
        # end def
    #==========================================
    
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        nov = self.InputNovel()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
#         print(f"Year: {nov[0]}")
#         print(f"DOI: {nov[1]}")
#         print(f"Name: {nov[2]}")
#         print(f"Author: {nov[3]}")
        for i in nov:
            print(i)
        # end def   



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
