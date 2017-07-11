def islucky(x):
	fl =0
	while x:
		y= x%10
		if y == 4 or y == 7:
			fl= 1
		else:
			fl=0
			break
		x/=10
	if fl:
		return True
	else:
		return False
n = input()
fl =0
for i in range(1,n+1):
	if islucky(i):
		if n%i ==0:
			fl =1
if fl :
	print "YES"
else:
	print "NO"
