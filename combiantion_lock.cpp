#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
  int n;
  scanf("%d",&n );
  char s1[1005],s2[1005];
  scanf("%s %s",&s1,&s2 );
  int cnt = 0;
  for(int i=0;i<n;i++)
  {
    int x= int(s1[i]);
    int y= int(s2[i]);
    int z = abs(x-y);
    int a = min(z,10-z);
    cnt+=a;
  }
  printf("%d\n",cnt );
}
