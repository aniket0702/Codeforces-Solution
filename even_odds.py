import math
x,y = map(int,raw_input().split())\
m=math.ceil(x/2);
if y<=m:
	print (y-1)*2+1
else:
	print (y-m)*2
