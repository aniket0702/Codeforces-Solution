t = input()
cnt =0
while t:
	x,y,z = map(int,raw_input().split())
	s = x+y+z
	if s>= 2:
		cnt+=1
	t-=1
print cnt