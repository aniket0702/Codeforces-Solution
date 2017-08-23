t= input()
for _ in range(t):
	n = input()
	l1=[]
	l2=[]
	l3 = []
	s = 0
	for i in range(n-1):
		x,y,z = map(str,raw_input().split())
		l1.append(x)
		l2.append(y)
		l3.append(int(z))
		s+=int(z)
	x=""
	for i in range(len(l1)):
		if l1[i] in l2:
			continue
		else:
			x = i
			break
	print l1[x] + " " + l2[x] + " "+ str(l3[x])
	for i in range(n-2):
		x= l1.index(l2[x])
		if x>=0:
			print l1[x] + " " + l2[x] + " "+ str(l3[x])
	print sn