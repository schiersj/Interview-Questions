#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
   string val = "1234";
   int val2 = 0;

   int j = 1;
   for (int i = 0; i < val.length()-1; ++i)
   {
      j *= 10;
   }

   for (int i = 0; i < val.length(); ++i)
   {
      val2 += (atoi(string(1,val[i]).c_str()))*j;
      j/=10;
   }

   cout << val2 << endl;

   return 0;
}
