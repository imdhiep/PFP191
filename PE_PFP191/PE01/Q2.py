class Main:
#====================f1====================
    def f1(self): #Count all line in file txt
# ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open("data_text.txt", "r") as f:
            data = f.readlines()
            print("The number of line:", len(data))
        
# end def
#====================f2====================
    def f2(self): #Print top 3 word
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open("data_text.txt", "r") as f:
            data = f.readlines()
        data_after_remove_n = []
        for text in data:
            text = text.split("\n")[0]
            text = text.strip()
            text = text.split(".")
            if "" in text:
                data_after_remove_n.append([text[0]])
            else:
                data_after_remove_n.append(text)
        data_special = [data_after_remove_n[0][0]]
        data_processing = []
        for i in range(1, len(data_after_remove_n)):
            if len(data_after_remove_n[i]) > 1:
                lst = []
                for j in data_after_remove_n[i]:
                    j = j.strip()
                    lst.append(j)
                text1 = " ".join(lst)
                data_processing.append(text1)
            else:
                data_processing.append(data_after_remove_n[i][0])
        
        data_list = []
        for string in data_processing:
            string = string.lower()
            word_list = string.split(" ")
            data_list.append(word_list)
        
        data_special = data_special[0].split(" ")
        for i in range(len(data_special)):
            if "(" in data_special[i]:
                data_special[i] = data_special[i][1:]
            if ")" in data_special[i]:
                data_special[i] = data_special[i][:-1]
            data_special[i] = data_special[i].lower()
        data_list.append(data_special)
        new_data_list = []
        for j in data_list:
            new_data_list += j
        set_new_data_lst = list(set(new_data_list))

        D = {word:0 for word in set_new_data_lst}
        for i in new_data_list:
            D[i] += 1
        D_sort = dict(sorted(D.items(), key=lambda item: item[1], reverse=True))
        keys = list(D_sort.keys())
        for i in range(3):
            print(f"{keys[i]}:{D_sort[keys[i]]}")
        
    # end def
    
    def f3(self): #Print data on the screen
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open("data_text.txt", "r") as f:
            data = f.read()
            print(data)
    # end def
    #================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        print("OUTPUT")
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