#include<bits/stdc++.h>
using namespace std;
int main()
{
  string s="aniket";
  int n,m;
  cin>>n>>m;
  string s;
  cin>>s;
  int arr[26]={0};
  for(int i=0;i<s.length();i++)
  {
    arr[s[i]-'a']++;
  }
  int p =0,c = 0,t = 0;
  for(int i=0;i<26;i++)
  {
    if(arr[i]!=0)
      p = arr[i];
    t += min(p,c);
    c = p-c;
  }
  if(t>=m)
    printf("YES\n" );
  else
    printf("NO\n" );
}
