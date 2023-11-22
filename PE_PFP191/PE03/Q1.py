import random

def main():
    number_range = int(input("Enter a range for the guess number:"))
    random_number = random.randint(0, number_range)
    while True:
        person_answer = input("Is " + str(random_number) + " too high(h), too low(l), correct(c):")
        if person_answer == "h":
            random_number = random.randint(0, random_number)
        elif person_answer == "l":
            random_number = random.randint(random_number, number_range)
        elif person_answer == "c":
            break
        else:
            person_answer = input("Is " + str(random_number) + " too high(h), too low(l), correct(c):")

    print(f"Welldone! The computer guessed your answer {random_number} correctly!")

if __name__ == "__main__":
    main()
