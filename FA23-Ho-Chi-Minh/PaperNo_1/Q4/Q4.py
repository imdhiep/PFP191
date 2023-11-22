#-----------------------------------------------------------------------------
def countWords(sentence, str):
    count = 0
    # Begin your statements here
    for word in sentence.split():
           if word.lower().endswith(str.lower()):
               count += 1
    # End your statements
    return count
#end countWords
#-----------------------------------------------------------------------------
#=============DO NOT ADD NEW OR CHANGE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("Test Q4 (3 marks)")
    sentence = input("Enter the sentence:")
    str = input("Enter a string:")
    print("OUTPUT:")
    count = countWords(sentence,str)
    print(f"{count}")
#end main
#=================DO NOT ADD NEW OR CHANGE THIS STATEMENTS =====================
if __name__ == '__main__':
    main()
