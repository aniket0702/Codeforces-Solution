#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n,m;
  scanf("%d %d",&n,&m );
  for(int i=1;1;i++)
  {
    int x = n*i;
    if(x%10 == 0 || x%10 == m)
      {printf("%d\n",i );
      break;}
  }
}
