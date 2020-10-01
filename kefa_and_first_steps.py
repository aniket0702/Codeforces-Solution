n = input()
l = list(map(int,input().split()))
cnt=1
i =0
m = 1
while i<n-1:
	if l[i]<=l[i+1]:
		cnt+=1
		if cnt>m:
			m = cnt
	else:
		cnt =1
	i+=1
print(m)
// Changing compatability from python 2.7 to python 3.0
