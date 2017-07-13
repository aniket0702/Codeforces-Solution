n,m,a,b = map(int ,raw_input().split())
s1 = 0
s1+= (n/m)*b
s1+= (n%m)*a
s2 = (n/m +1)*b
print min(s1,s2)