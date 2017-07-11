import sys
s = raw_input()
s = s.lower()
y = "aeiouy"
for i in s:
	if i not in y:
		sys.stdout.softspace = False
		print "."+i,
