x,y = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
i = 1
cnt =0
while i < y  :
	# if i<y:
	i+=l[i-1] 
	# print i
if i == y:
	print "YES"
else:
	print "NO"