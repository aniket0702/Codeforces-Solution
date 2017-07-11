def primecheck(x):
	cnt=0
	for i in range(2,x/2 +1):
		if x%i == 0:
			cnt+=1
			break
	if cnt :
		return 1
	else:
		return 0


n = input()
for i in range(4,n):
	if primecheck(i) == 1 and primecheck(n-i) == 1:
		print str(i) + " "+ str(n-i)
		break
