k,n,w = map(int,raw_input().split())
x = k*(w*(w+1))/2
if (x-n)>0:
	print x-n
else:
	print 0