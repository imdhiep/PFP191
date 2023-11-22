#Q1.1 Create a new empty text file named 'sales.txt'
def program1():
    f = open('sales.txt', 'w')
    f.close()

#Q1.2 Create File with a DateTime
def program2():
    import os
    import datetime

    now = datetime.datetime.now()

    filename = now.strftime("%d-%m-%Y")
    f = open(filename + ".txt", 'w')
    f.close()
    print(f"created {filename}.txt")

    filename1 = now.strftime("%d-%m-%Y-%H-%M-%S")
    a = open(filename1 + ".txt", 'w')
    a.close()
    print(f"created {filename1}.txt")

    filename2 = now.strftime("%d-%m-%Y-%H-%M-%S")
    b = open(filename2 + ".txt", 'w')
    b.close()
    print(f"created {os.path.abspath(filename2)}.txt")

#Q1.3 Create a file with Permission
def program3():
    import os

    file_name = "sample.txt"
    try:
        f = open(file_name, 'w')
        
        print("""    1: Read-Only
        2: Read and Write for Owner and Group, Read-Only for Others
        3: Read and Write for Owner, Read-Only for Group and Others
        4: Read, Write, and Execute for Owner, Read and Execute for Group and Others
        5: Read, Write, and Execute for Owner and Group, Read-Only for Others
        6: Full Permissions for Owner, Group, and Others""")

        while True:
            n = input("Enter a number: ")
            print()
            if not n.isdigit() or int(n) < 1 or int(n) > 7:
                print("Invalid number")
            else:
                n = int(n)
                break
        if n == 1:
            permission = 0o444
            os.chmod(file_name, permission)
        elif n == 2:
            permission = 0o664
            os.chmod(file_name, permission)
        elif n == 3:
            permission = 0o644
            os.chmod(file_name, permission)
        elif n == 4:
            permission = 0o755
            os.chmod(file_name, permission)
        elif n == 5:
            permission = 0o774
            os.chmod(file_name, permission)
        elif n == 6:
            permission = 0o777
            os.chmod(file_name, permission)

        print(f'{file_name} has been created with {oct(permission)} permission')
        
        f.close()
    except PermissionError:
        print('This file has been created with Read Only permission, cannot overwrite.')
        print('Do you want to delete this file? (y/n)')
        while True:
            s = input('Enter y or n: ')
            if s != 'y' and s != 'n':
                print('Please enter letter again')
            else:
                break
        if s == 'y':
            if os.path.exists(file_name):
                os.chmod(file_name, 0o777)
                os.remove(file_name)
                print(f'{file_name} has been removed')
                
#Q2.1 Write to a new file
def program4():
    f = open("Newfile.txt","w")
    f.write(input("Enter text that you want to write in new file: "))
    f.close()

    f = open("Newfile.txt", "r")
    print(f.read())
    
#Q2.2 Writing to an existing file
def program5():    
    f = open("Newfile.txt","a")
    f.write(input("Enter extra text that you want to write in previous file: "))
    f.close()

    f = open("Newfile.txt", "r")
    print(f.read())

#Q2.3 Write a list of line to a file
def program6():
    lines = []
    empty_line = False
    print("Input lines until you press 3 times Enter")
    while True:
        line = input()
        if line == '':
            if empty_line:
                break
            empty_line = True
            continue
        empty_line = False
        lines.append(line)
    lines = '\n'.join(lines)

    f = open('Newfile.txt', 'w')
    f.write(lines)
    f.close()

    f = open('Newfile.txt', 'r')
    print(f.read())

#Q3.1: Seek the Beginning of the File
def program7():
    f = open('Newfile.txt', 'w+')
    f.write('My First line\n')
    f.write('My Second line')
    f.seek(0)
    print(f.read())
    f.close()

#Q3.2: Seek the end of the file
def program8():
    f = open('Newfile.txt', 'r+')
    f.seek(0, 2)
    f.write('\nThis content is added to the end of the file')
    f.seek(0)
    print(f.read())
    f.close()

#Q3.3: Seek from the current position
def program9():
    with open("Newfile.txt", "rb") as f:
        f.seek(3)
        print(f.read(5).decode("utf-8"))
        
        f.seek(10, 1)
        print(f.read(6).decode("utf-8"))

#Q3.4: Seek backward with negative offset
def program10():
    with open("Newfile.txt", "rb") as f:
        print(f.read(8).decode('utf - 8'))
        f.seek(-5,1)
        print(f.read(10).decode('utf - 8'))
        
#Q3.5: Use tell() Function to get file handle position
def program11():
    with open("Newfile.txt", "r+") as f:
        f.seek(0,2)
        print("file handle at: ", f.tell())
        
        f.write("\nDemonstrating tell")
        print("file handle at: ", f.tell())
        
        f.seek(0)
        print("file handle at: ", f.tell())
        
        print("***Printing file content***")
        print(f.read())
        print("***Done***")
        with open("Newfile.txt", "r+") as f:
            f.seek(0,2)
        print("file handle at: ", f.tell())
        
        f.write("\nDemonstrating tell")
        print("file handle at: ", f.tell())
        
        f.seek(0)
        print("file handle at: ", f.tell())
        
        print("***Printing file content***")
        print(f.read())
        print("***Done***")

#Q4.1 Rename a file after checking whether it exists
def program12():
    import os
    file_name = "Test0.txt"
    new_file1 = "Test1.txt"
    new_file2 = "Test2.txt"
    if os.path.exists(file_name):
        os.rename(file_name, new_file1)
        print(f"{file_name} is existed and has been rename to {new_file1}")
    else:
        open(file_name, "w").close()
        os.rename(file_name, "Test2.txt")
        print(f"{file_name} is not existed, new file is created and has been rename to {new_file1}")

#Q4.2: Rename multiple file in Python
def program13():
    import os

    a = input("Enter path of folder: ")
    folder_path = r'{}\\'.format(a)
    count = 1
    for file_name in os.listdir(folder_path):
        old_name = folder_path + file_name
        new_name = folder_path + "sales_" + str(count) + ".txt"
        
        os.rename(old_name, new_name)
        count += 1
    print("All Files Renamed")
    print("New Names are ")
    print(os.listdir(folder_path))

#Q4.3 Renaming only a list of files in a folder
def program14():
    import os

    a = input("Enter path of your folder: ")
    folder_path = r'{}\\'.format(a)

    n = int(input("Enter the number of files you want to rename: "))
    list_file = []

    for i in range (0,n):
        file_name = input("Enter name of file: ")
        list_file.append(file_name)
    print(list_file)

    new_list = []
    for file_name in os.listdir(folder_path):
        if file_name in list_file:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                new_name = input("Enter new name for {}: ".format(file_name))
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                new_list.append(os.path.basename(new_path))
    print("All new names are ", new_list)

#Q4.4 Renaming files with a timestamp
def program15():
    import os
    import datetime

    file_name = input("Enter your file name: ")

    if os.path.exists(file_name):
        f = open('{}'.format(file_name), 'r+')
        f.close()
    else:
        f = open('{}'.format(file_name), 'w')
        f.close()
        
    now = datetime.datetime.now()
    last_name = file_name.split(".")[0] + now.strftime("%d - %m - %Y") + ".txt"
    os.rename(file_name, last_name)
    print(f'{file_name} has been change to {last_name}')

#Q4.5 Renaming the Extension of the Files
def program16():
    import os

    a = input('Enter path of folder: ')
    folder_path = r'{}\\'.format(a)
    print('Before rename\n', os.listdir(folder_path))
    b = input("Enter the new extension of the Files (including '.'): ")
    for file_name in os.listdir(folder_path):
        old_name = folder_path + file_name
        new_name = folder_path + file_name.split(".")[0] + b
        os.rename(old_name, new_name)
    print('After rename\n', os.listdir(folder_path))

#Q4.6 Renaming and then moving a file to a new location
def program17():
    import os

    a = input('Enter old path of folder: ')
    old_folder_path = r'{}\\'.format(a)

    b = input('Enter new path of folder: ')
    new_folder_path = r'{}\\'.format(b)

    file_name = input('Enter name of file: ')
    new = input('New name of file: ')
    if os.path.exists(file_name):
        old_name = old_folder_path + '{}'.format(file_name)
        new_name = new_folder_path + '{}'.format(new)
    else:
        f = open(file_name, 'w')
        old_name = old_folder_path + '{}'.format(file_name)
        new_name = new_folder_path + '{}'.format(new)
        f.close()

    os.rename(old_name, new_name)
    print('Rename and change position successfully')

import time
    
programs = [program1, program2, program3, program4, program5, program6, program7, program8, program9, program10, program11, program12, program13, program14, program15, program16, program17]

while True:
    print("Menu:")
    print("1. Q1.1 Create a new empty text file named 'sales.txt'")
    print("2. Q1.2 Create File with a DateTime")
    print("3. Q1.3 Create a file with Permission")
    print("4. Q2.1 Write to a new file")
    print("5. Q2.2 Writing to an existing file")
    print("6. Q2.3 Write a list of line to a file") 
    print("7. Q3.1: Seek the Beginning of the File")
    print("8. Q3.2: Seek the end of the file")
    print("9. Q3.3: Seek from the current position")
    print("10. Q3.4: Seek backward with negative offset")
    print("11. Q3.5: Use tell() Function to get file handle position")
    print("12. Q4.1 Rename a file after checking whether it exists")
    print("13. Q4.2: Rename multiple file in Python")
    print("14. Q4.3 Renaming only a list of files in a folder")
    print("15. Q4.4 Renaming files with a timestamp")
    print("16. Q4.5 Renaming the Extension of the Files")
    print("17. Q4.6 Renaming and then moving a file to a new location")
    
    choice = input("Choose program to run (1-17) or 'e' to exit: ")
  
    if choice == 'e':
        break
    
    choice = int(choice)
    if 1 <= choice <= 17:
        programs[choice-1]()
        time.sleep(1)
    else:
        print("Invalid choice!")



