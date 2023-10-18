#include<stdio.h>
void matrix();
int main()
{
	matrix();
	return 0;
}
void matrix()
{
	int n,r,c,i,j,k,num1[2][2],num2[2][2],result[2][2];
	printf("enter total number of row");
	scanf("%d",&r);
	printf("enter total number of col");
	scanf("%d",&c);
	printf("\nfirst array");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			scanf("%d",&num1[i][j]);
		}
	}
	printf("\n second array");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			scanf("%d",&num2[i][j]);
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
		result[i][j]=0;	
	}
}
	
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
	
			for(k=0;k<c;k++)
			{
				result[i][j]+=num1[i][k]*num2[k][j];
			}
		}
	}
	printf("matrix multiplication\n");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d\t",result[i][j]);
		}printf("\n");
	}
	
}
