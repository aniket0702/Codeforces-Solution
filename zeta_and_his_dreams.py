n,m,q = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
lt= [list]*(n+1)
for i in range(m):
	x,y = map(int,raw_input().split())
	l[x].append(y)
	l[y].append(x)
