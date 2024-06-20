/*
#include<stdio.h>
int main()
{
int a=4,b=2,c;
a=a+1;
b=b-1;
c=a^b;
printf("%d",c);
}
*/
/*
int main()
{
 int a=5;
for(int i=0;i<=5+2;i++);
  {
  printf("hi");
  }
}
*/
/*
#include<stdio.h>
int main()
{
int a=5,b=6,c=7;
printf("%d",printf("abc"));
}
*/
/*
#include<stdio.h>
#include<string.h>
int main()
{
   int c;
   char a[5]="hello";  //Line 1
   char b[5]="car";    //Line 2
   c=strlen(a);          
   printf("%d %s %s",c,b,a); //Line 3
}*/
/*
int a[3][3]={{2,8,7},{1,8,9},{3,6,5}};
printf("%d %d %d", *(*(a+1)), **a, *(*(a+2)+2));
*/
int main()
{
int a[5]={5,9,2,1,3},*b;
b=a+2;
printf("%d %d %d",*(b+1),a[*(a+3)],*b+2);
}

