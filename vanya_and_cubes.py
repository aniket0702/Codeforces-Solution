n = input()
i = 1
l = 0
while 1:
	s = ((i*(i+1)*(2*i + 1))/6 + (i*(i+1))/2)/2
	# print s	
	if s <= n:
		l+=1
		i+=1
	else:
		print l
		break