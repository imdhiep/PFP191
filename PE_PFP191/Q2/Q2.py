def prime_factors(n):
    n = int(n)
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        fhand = open(fileName)
        for line in fhand:
            lst = line.split()
            print('\n'.join(lst))
        pass
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        fhand = open(fileName)
        for line in fhand:
            lst = line.split()
            for x in lst:
                y = prime_factors(x)
                y = [str(x) for x in y]
                print(x, '=', ' x '.join(y))




        pass
        # end def
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        fileName = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(fileName)
        elif choice == 2:
            self.f2(fileName)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
