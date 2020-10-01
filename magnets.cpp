#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// using fast I/O for speed improvisation
	int n;
	cin>>n;
	int prev;
	cin>>prev;
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
	cout<<cnt<<endl;
return 0;	
}
