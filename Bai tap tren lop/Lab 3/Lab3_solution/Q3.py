#Q3.1  
def count_uppercase(file_name):
  count = 0
  with open(file_name, 'r') as f:
    for line in f:
      for character in line:
        if character.isupper():
          count += 1

  print("Number of uppercase characters:", count)

count_uppercase('Q3.txt')

#Q3.2
def count_words(file_name, target_words):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.lower() in target_words:
                    count += 1
    print("Number of occurrences of 'this' and 'these':", count, end='\n')

target_words = ["this", "these"]
count_words('Q3.txt', target_words)