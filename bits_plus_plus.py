t = input()
x=0
while t:
	s = raw_input()
	if s == "++X" or s == "X++":
		x+=1
	else:
		x-=1
	t-=1
print x