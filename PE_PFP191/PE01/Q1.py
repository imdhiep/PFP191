class Main:
#====================f1====================
    def f1(self, password): #check valid password
# ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        x = True
        while x:
            if len(password) < 6 or len(password) > 12:
                break
            elif not any(char.isalpha() and char.islower() for char in password):
                break

            elif not any(char.isalpha() and char.isupper() for char in password):
                break
            elif not any(char.isnumeric() for char in password):
                break
            elif not any(char in ["$", "#", "@"] for char in password):
                break
            else:
                print("Valid password")
                x=False
                break

        if x:
            print("Invalid password")
# end def
    #================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        password = input("Enter the password:")
        print("OUTPUT")
        self.f1(password)
        print("FINISH")
    
main = Main()
main.main()