def gcd(n,m):
	x= min(n,m)
	if x==0:
		return max(n,m)
	for i in range(x,0,-1):
		if n%i ==0 and m%i == 0:
			return i

a,b,c = map(int,raw_input().split())
i = 1
while i:
	if i%2 == 1:
		x= gcd(a,c)
		if x<=c:
			c-=x
		else:
			print "1"
			break
		i+=1
	else:
		x = gcd(b,c)
		if x<=c:
			c-=x
		else:
			print "0"
			break
		i+=1