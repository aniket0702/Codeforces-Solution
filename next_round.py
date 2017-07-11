x,y = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
l=sorted(l)
l  = l[::-1]
z = l[y-1]
cnt=0
for i in l:
	if i>=z and i>0:
		cnt+=1
print cnt