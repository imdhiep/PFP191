# file = open('data.txt', 'r')
# content = file.read().split(' ')
# content = [int(i) for i in content]
# 
# for number in content:
#     a = []
#     i = 2
#     num = number
#     while i <= number:
#         if number % i == 0:
#             a.append(i)
#             number = number // i
#             i -= 1
#         i += 1
#             
#     print(f'{num} = ', end='')
#     for i in range(len(a)):
#         print(f'{a[i]} x ', end='')
#     print(number)

file = open('data.txt', 'r')
content = file.read().split(' ')
content = [int(i) for i in content]


for number in content:
    s = str(number) + ' = '
    i = 2
    while i*i <= number:
        if number % i == 0:
            s += str(i) + ' x '
            number = number // i
        else:
            i += 1 
    s += str(number)
    print(s)


