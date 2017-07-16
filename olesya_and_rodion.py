n,t = map(int,raw_input().split())
i = 10**(n-1)
j = 10 **n 
fl =0
while i<j:
	if i%t == 0:
		print i
		break
	i+=1
if i ==j:
	print "-1"
