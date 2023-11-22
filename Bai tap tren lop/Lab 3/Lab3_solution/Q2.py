#Q2.1
def count_words(file_name):
  with open(file_name, 'r') as f:
    data = f.read()
    words = data.split()
    num_words = len(words)
    print("Number of words in text file:", num_words)

count_words('Q2.txt')
#Q2.2
def display_words():
  with open('Q2.txt', 'r') as file:
    for line in file:
      words = line.split()    
      for word in words:
        if len(word) < 4:
          print(word, end=' ')

display_words() 