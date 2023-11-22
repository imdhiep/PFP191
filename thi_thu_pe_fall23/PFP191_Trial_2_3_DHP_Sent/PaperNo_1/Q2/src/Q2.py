import random
class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        i = 0
        j = int(number)
        guess = ''
        while guess != 'c':
            n = random.randint(i, j)
            guess = input(f'Is {n} too high(h), too low (l), or correct(c): ')
            if guess == 'h':
                j = n
            elif guess == 'l':
                i = n
            else:
                print("correctly!")
                break

    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
