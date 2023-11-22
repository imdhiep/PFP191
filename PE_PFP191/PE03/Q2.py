import os
def main():
    file_name = input("Enter the file name:")
    exist = os.path.exists(file_name)
    if exist == False:
        while True:
            file_name = input("File not exist, please try again:")
            exist = os.path.exists(file_name)
            if exist:
                break
    
    elif exist==True:
        with open(file_name, "r") as f:
            text = f.read()
        option = int(input("Enter the option (1. Content - 2. Compute):"))
        if option == 1:
            print(f"Content: {text}")
        elif option == 2:
            lst = text.split(",")
            new_lst = []
            for i in lst:
                if i[0] == " ":
                    new_lst.append(i[1:])
                else:
                    new_lst.append(i)
            rs = 0
            for i in new_lst:
                if i[0] == "D":
                    rs += int(i[2:])
                elif i[0] == "W":
                    rs -= int(i[2:])
            
            print(rs)
if __name__ == "__main__":
    main()