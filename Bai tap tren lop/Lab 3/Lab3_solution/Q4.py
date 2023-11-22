#Q4.1
def hash_display(file_name):
    with open(file_name, 'r') as f:
        while True:
            char = f.read(1)
            if not char:
                break
            print(char, end='#')

hash_display('Q4.1.txt')

print()
#Q4.2
def j_to_i(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    content = content.replace('J', 'I')
    print(content, end='\n')

j_to_i('Q4.2.txt')