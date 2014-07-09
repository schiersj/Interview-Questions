def is_palindrome(string):
    tmp = string[::-1] # invert the string
    if tmp == string:
      print string

def main():
   f = open('q1.txt')

   content = f.readlines()

   lst = []
   for row in content:
      lst.append(row.replace('\n','').split(','))

   for row in lst:
      for r in row:
         is_palindrome(r)

if __name__ == '__main__':
   main()
