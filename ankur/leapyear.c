#include<stdio.h>
#include<conio.h>
void main()
{
int a;
clrscr();
printf("write the year");
scanf("%d",&a);
if(a%4==0)
{
if(a%100==0)
{
if(a%400==0)
printf("%d ia a leap year",a);
else
printf("%d is not a leap year",a);
}
else
{
printf("%d is a leap year",a);
}
}
else
{
printf("%d is not a leap year",a);
}
getch();
}


