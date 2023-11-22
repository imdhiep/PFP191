class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import random
        start = 0 
        end = int(number)
        while True:
            computer_guess = int(random.uniform(start, end))
            guess = input((f'Is {computer_guess} too high(h), too low(l), or correct(c): '))

            if guess == 'l':    
                start = computer_guess + 1
            elif guess == 'h':  
                end = computer_guess - 1
            elif guess == 'c': 
                print(f'Welldone! The computer guessed your number {computer_guess} correctly!')
                break
#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
