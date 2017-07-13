n = input()
s = raw_input()
s= s.lower()
st= set(s)
if len(st) == 26:
	print "YES"
else:
	print "NO"