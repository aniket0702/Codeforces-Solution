n = input()
l = list(map(int,raw_input().split()))
m = 0
mi = n-1
for i in range(n):
	if l[i]> l[m]:
		m=i
	if l[i]<=l[mi]:
		mi = i
if mi>m:
	print (n+m-mi-1)
else:
	print (n+m-mi-2)