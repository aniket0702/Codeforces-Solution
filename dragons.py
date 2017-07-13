s,n = map(int,raw_input().split())
fl =1
l=[]
for i in range(n):
	x,y = map(int,raw_input().split())
	l.append([x,y])

l = sorted(l)
# print l
for i in range(n):
	if s > l[i][0]:
		s+=l[i][1]
		# print s
	else:
		fl =0	
		break
if fl:
	print "YES"
else:
	print "NO"