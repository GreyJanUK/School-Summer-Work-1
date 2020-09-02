// Demonstration of iteration by running a bubble sort - GJUK
#include <iostream>
using namespace std;

int main () {
   int i, j,temp,pass=0;
   int a[12] = {10,2,0,14,43,25,18,1,5,45,132,15}; // Number of values in the array followed by the array with the numbers to be sorted
   cout <<"Input list ...\n";
   for(i = 0; i<12; i++) {
      cout <<a[i]<<"\t";
   }
cout<<endl;
for(i = 0; i<12; i++) {
   for(j = i+1; j<12; j++)
   {
      if(a[j] < a[i]) {
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
      }
   }
pass++;
}
cout <<"Sorted Element List ...\n";
for(i = 0; i<12; i++) {
   cout <<a[i]<<"\t";
}
cout<<"\nNumber of passes (iterations) taken to sort the list: "<<pass<<endl;
return 0;
}
