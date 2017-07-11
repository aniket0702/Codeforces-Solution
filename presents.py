n = input()
l = list(map(int,raw_input().split()))
lt = [0]*n
for i in range(n):
	lt[l[i]-1] =i+1

for i in lt:
	print i,
