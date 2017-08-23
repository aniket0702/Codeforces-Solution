n,a,b,c = map(int,raw_input().split())
def retsum(x,y):
	r =n-( x*a + y*b )
	return r

def process():
	x=0
	m=0
	while x<(n/a)+1:
		y=0
		while y<(n/b)+1:
			s  = retsum(x,y)
			# print s
			if s>=0 and s%c == 0:
				z= s/c
				m = max(m,x+y+z)
			y+=1
		x+=1
	print m

if n%min(a,b,c) == 0:
	print n/min(a,b,c)
else:
	process()
