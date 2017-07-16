n = input()
l = list(map(int,raw_input().split()))
m = l[0]
mn = l[0]
cnt = 0
for i in l:
	if i >m :
		m=i
		cnt+=1
	if i<mn:
		cnt+=1
		mn = i

print (	cnt)