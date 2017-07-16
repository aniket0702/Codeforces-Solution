n,t = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
l =  sorted(l)
m =float(0)
for i in range(0,n-1):
	m = max(l[i+1]-l[i],m)
m = float(m)/2
if l[0] != 0:
	m = max(m,l[0]-0)
if l[n-1]!=t:
	m = max(m,t-l[n-1])
m = float(m)
print str(m)+'0'*8