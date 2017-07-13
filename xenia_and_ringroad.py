n,m = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
cnt = l[0] -1
for i in range(1,m):
	if l[i]>= l[i-1]:
		cnt+=l[i]-l[i-1]
	else:
		cnt+= n+l[i]-l[i-1] 
print cnt
