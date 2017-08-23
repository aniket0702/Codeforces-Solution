n  =input()
l  =list(map(int,raw_input().split()))
cnt = 0
for i in range(0,n-2):
	for j in range(i+1,n-1):
		if l[j]>l[i]:
			for k in range(j+1,n):
				if l[i]<l[j] and l[j]>l[k]:
					cnt+=1
print cnt%1000000007