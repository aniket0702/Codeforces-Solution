import sys
s2 = raw_input()
s1 = raw_input()
for i,j in zip(s1,s2):
	if i==j:
		sys.stdout.softspace = False
		print "0",
	else:
		sys.stdout.softspace = False
		print "1",