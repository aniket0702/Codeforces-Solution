t = input()
while t:
	x = raw_input()
	y = len(x)
	if y <= 10:
		print x
	else:
		print x[0]+str(y-2)+x[y-1]
	t-=1