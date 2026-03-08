#include<stdio.h>
void main(){
    int j,i,n=5;
    int a=[10,20,30,5,7];
    for(i=0;i<n-1;i++)
    {
        int minindex=i;
        for(j=i+1;j<n-1;j++)
        {
            if a[minindex]>=a[j];{
                minindex=j;
            }
        }
    }
}