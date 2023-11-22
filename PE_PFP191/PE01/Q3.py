# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Book:
    def __init__(self, rollnumber, name, year, doi):
        self.rollnumber = rollnumber
        self.name = name
        self.year = year
        self.doi = doi
    
    def get_rollnumber(self):
        return self.rollnumber
    
    def set_rollnumber(self):
        return self.rollnumber

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_doi(self):
        return self.doi

    def set_doi(self, doi):
        self.doi = doi

    def display_info(self):
        print(f"Year: {self.year}")
        print(f"DOI: {self.doi}")
        print(f"Name: {self.name}")

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputListBook(self):
        n = int(input('Enter the number of books: '))
        books = []
        for i in range(n):
            rollnumber = int(input("Enter rollnumber:"))
            name = input("Enter name:")
            roi = int(input("Enter ROI:"))
            years = int(input("Enter year:"))
            new_book = Book(rollnumber, name, years, roi)
            books.append(new_book)
        return books
        # end def

    #====================f1====================
    def f1(self): #print information
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================
        for book in bookList:
            print("Rollnumber:", book.rollnumber)
            print("name:", book.name)
            print("ROI:", book.doi)
            print("Year:", book.year)
            
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
                    
        # end def
    #==========================================

    #====================f2====================
    def f2(self): #sort
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================
        sort_booklist = sorted(bookList, key=lambda x: x.name)
        for book in sort_booklist:
            print("Rollnumber:", book.rollnumber)
            print("name:", book.name)
            print("ROI:", book.doi)
            print("Year:", book.year)
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
                   
        # end def
    #==========================================



    #====================f3====================
    def f3(self): #filter
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        for book in bookList:
            if book.year >= 2010:
                print("Rollnumber:", book.rollnumber)
                print("name:", book.name)
                print("ROI:", book.doi)
                print("Year:", book.year)
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
        # end def
    #==========================================


#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
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

