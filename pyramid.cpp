// print a perimid of characters

//   x
//  xxx
// xxxxx

// input width of base and char

#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
   char star;
   int width;
   int numSpaces = 0;
   cout << "Enter the width and char: ";
   cin >> width >> star;

   for (int i = 0; i < width; i++)
   {
      if ((i % 2) != 0)
      {
         numSpaces = (width - i) / 2; // Calculate number of spaces to add
         for (int j = 0; j < numSpaces; j++) // Print spaces
            cout << " ";
         for (int k = 0; k < i; k++) // Print characters
            cout << star;
         cout << endl;
      }
   }
   return 0;
}
