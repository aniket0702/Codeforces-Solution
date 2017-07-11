x,y = map(int,raw_input().split())
if x%2 == 0:
	m =x/2
else:
	m = x/2 + 1
if y<=m:
	print (y-1)*2+1
else:
	print (y-m)*2