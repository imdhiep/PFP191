class Main:
    
    #====================f1====================
    def f1(self, month):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        l1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        l2 = []
        for i in l1:
            i = i.lower()
            l2.append(i)
        if month in l1 or month in l2:
            print("{} is a month".format(month))
        else:
            print("{} not a month name".format(month))
        # end def


    #====================f2====================
    def f2(self, month):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if month in ["January", "March", "May", "July", "August", "October", "December", "january", "march", "may", "july", "august", "october", "december"]:
            print("31")
        elif month in ["April", "June", "September", "November", "april", "june", "september", "november"]:
            print("30")
        elif month == "February" or "february":
            print("28/29")
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
