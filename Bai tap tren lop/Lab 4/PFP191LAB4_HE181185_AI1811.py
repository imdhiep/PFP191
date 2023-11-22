class Main:
#==========Input Value================
   def InputList(self):
       input_count1 = int(input("Enter the number of elements in list 1: "))
       input_list1 = []
       for i in range(input_count1):
           input_value = input("Enter element number {} in list 1: ".format(i + 1))
           input_list1.append(input_value)

       input_count2 = int(input("Enter the number of elements in list 2: "))
       input_list2 = []
       for i in range(input_count2):
           input_value = input("Enter element number {} in list 2: ".format(i + 1))
           input_list2.append(input_value)

       print("Original list")
       print(input_list1)
       print(input_list2)
       return input_list1, input_list2
#===========Def in Selection ============
   def longestCommonSubsequence(self, a, b):
       m = len(a)
       n = len(b)

       L = [[0] * (n+1) for _ in range(m+1)]

       for i in range(m):
           for j in range(n):
               if a[i] == b[j]:
                  L[i+1][j+1] = L[i][j] + 1
               else:
                  L[i+1][j+1] = max(L[i+1][j], L[i][j+1])

       return L[-1][-1]

   def firstNonRepeating(self, arr):
       count = {}
       for element in arr:
           if element in count:
               count[element] += 1 
           else:
               count[element] = 1

       for element in arr:
           if count[element] == 1:
               return element
       return None

   def sort_list(self, lst):
       return sorted(lst)

   def find_pairs(self, lst, target):
       result = []
       s = set()

       for i in range(len(lst)):
           if (target - lst[i]) in s:
               result.append([lst[i], target - lst[i]]) 
           s.add(lst[i])
       return result

   def group_elements(self, lst):
       result = {}

       for i in lst:
           if i in result:
               result[i].append(i)
           else:
               result[i] = [i]
       return result

   def merge_dicts(self, *dicts):
       result = {}

       for dict in dicts:
           for key, value in dict.items():
               if key in result:
                  result[key].extend(value) 
               else:
                  result[key] = value

       return result

   def invert_dict(self, d):
       inverse = {}

       for key, values in d.items():
           for value in values:
               if value in inverse:
                  inverse[value].append(key)
               else:
                  inverse[value] = [key]

       return inverse

   def f1(self, lst1, lst2):
       return self.longestCommonSubsequence(lst1, lst2)

   def f2(self, lst):
       return self.firstNonRepeating(lst)

   def f3(self, lst):
       return self.sort_list(lst)

   def f4(self, lst, target):
       return self.find_pairs(lst, target)

   def f5(self, lst):
       return self.group_elements(lst)

   def f6(self, dict1, dict2):
       return self.merge_dicts(dict1, dict2)

   def f7(self, d):
       return self.invert_dict(d)
#========Selection==============
   def main(self):
      print(" 1. Q1")
      print(" 2. Q2")
      print(" 3. Q3")
      print(" 4. Q4")
      print(" 5. Q5")
      print(" 6. Q6")
      print(" 7. Q7")
      print(" 0. Exit")
      print(" Your selection (0 -> 7): ")
      choice = int(input())
      
      if choice == 1:
          lst1, lst2 = self.InputList()
          print(self.f1(lst1, lst2))

      elif choice == 2:
          lst = self.InputList()
          print(self.f2(lst))

      elif choice == 3:
          lst = self.InputList()
          print(self.f3(lst))

      elif choice == 4:
          lst = self.InputList()
          target = int(input("Enter target: "))
          print(self.f4(lst, target))

      elif choice == 5:
          lst = self.InputList()
          print(self.f5(lst))

      elif choice == 6:
          dict1 = {}
          dict2 = {}
          print(self.f6(dict1, dict2))

      elif choice == 7:
          d = {}
          print(self.f7(d))

      elif choice == 0:
          print("Exiting...")

      else:
          print("Wrong selection")

if __name__ == '__main__':
  main = Main()
  main.main()
