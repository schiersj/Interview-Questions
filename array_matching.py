def check2(array,stuff):

   flag = False

   num = len(array)-1

   for i in range(num):
      if stuff.index(array[i]) == stuff.index(array[i+1])-1:
         flag = True
      else:
         flag = False

   print flag

def main():

   stuff = "Hello;everybody;how;are;we;all;doing;today"

   ar1 = ["everybody","how","are"]
   ar2 = ["everybody","are"]

   ar3 = stuff.split(';')

   check2(ar1,ar3)
   check2(ar2,ar3)

if __name__ == '__main__':
   main()
