#Q1
#Q1.1
def read_file_lines(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            print(line, end='')

read_file_lines('Q1.1.txt')

#Q1.2
def count_non_t_lines(file_name):
    count = 0
    with open(file_name) as f:
        for line in f:
            if not line.lower().startswith('t'):
                count += 1
    return count

num_lines = count_non_t_lines('Q1.2.txt')
print("\nNumber of lines not starting with 't':", num_lines)