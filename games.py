n = input()
l1= []
l2 = []
cnt = 0
for i in range(n):
	x,y = map(int,raw_input().split())
	l1.append(x)
	l2.append(y)
for i in range(n):
	for j in range(n):
		if l1[i] == l2[j]:
			cnt+=1

print cnt
