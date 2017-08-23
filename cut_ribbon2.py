s,a,b,c = map(int,raw_input().split())
def process(n):
	if n == s:
		return 0
	elif n>s:
		return -4000
	x,y,z = -4000,-4000,-4000
	x = process(n+a)
	y= process(n+b)
	z = process(n+c)
	return max(x,y,z)+1
c = process(0)
print c












