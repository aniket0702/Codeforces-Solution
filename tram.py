n = input()
m = 0
s = 0
while n:
	x,y= map(int,raw_input().split())
	s=s+y-x
	if s >m:
		m = s
	n-=1
print m