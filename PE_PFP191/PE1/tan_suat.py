class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        data = open(fileName, 'r')
        content = data.read()
        print(content)
        pass
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        data = open(fileName, 'r')
        content = data.readlines()
        print(len(content))
        print(content)
        pass
        # end def

    def f3(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import re
        file = open(fileName, 'r')
        content = file.read()
        list1 = content.split()
        words = re.findall(r'\b\w+\b', content)
        
        dict2 = {}
        for word in words:
            if word not in dict2:
                dict2[word] = 1
            else:
                dict2[word] +=1
        
        big_list = []
        for key, value in dict2.items():
            small_list = key,value
            small_list = list(small_list)
            big_list.append(small_list)
        big_list.sort(key = lambda x: (x[1], x[0]))
        for i in range(len(big_list)-1, len(big_list) - 11, -1):
            str1 = "{} {}".format(big_list[i][0], big_list[i][1])
            print(str1)        


#         text = content.translate(str.maketrans('', '', string.punctuation))
#         words = text.split()
#         new_words = []
#         for word in words:
#             if "-" in word:
#                 new_words.extend(word.split("-"))
#             else:
#                 new_words.append(word)
#         print(new_words)
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
        elif choice == 3:
            self.f3(fileName)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

