class Main:
    
    #====================f1====================
    def f1(self, month):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        temp = month
        month = month.strip()
        month = month.lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        if month in months:
            print(f"{temp} is a month")
        else:
            print(f"{temp} not a month name")
        pass
        # end def


    #====================f2====================
    def f2(self, month):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        month = month.strip()
        month = month.lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        dates = [31,'28/29', 31,30,31,30,31,31,30,31,30,31]
        if month in months:
            index = months.index(month)
            date = str(dates[index])
            print(date)
        else:
            pass
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
        month = input("Input the name of Month: ")
        print("OUTPUT")
        if choice == 1:
            self.f1(month)
        elif choice == 2:
            self.f2(month)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
