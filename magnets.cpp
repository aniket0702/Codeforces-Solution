#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	scanf("%d",&n);
	int prev;
	scanf("%d",&prev);
	int cnt = 1;
	for(int i=0;i<n-1;i++)
	{
		int x;
		scanf("%d",&x);
		if(prev!=x)
		{
			cnt+=1;
			prev = x;
		}
	}
	printf("%d\n",cnt);	
}