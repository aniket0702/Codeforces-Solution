#include<bits/stdc++.h>
using namespace std;
int s,a,b,c;
int process(int n)
{
	if(n == s)
		return 0;
	else if (n>s)
		return -4000;
	int x = process(n+a);
	int y = process(n+b);
	int z = process(n+c);
	return max(max(x,y),z)+1;
}
int main()
{
	scanf("%d %d %d %d",&s,&a,&b,&c);
	int c = process(0);
	printf("%d\n",c);

}