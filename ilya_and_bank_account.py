n = raw_input()
x = len(n) #a list of size n is initialised with 0
if n[0] != "-":
	print n
else:
	if int(n) >= -10:
		print "0"
	elif x>2:
		if n[x-1] > n[x-2]:
			print str(int(n[:x-1]))
		else:
			print str(int(n[:x-2] + n[x-1]))
