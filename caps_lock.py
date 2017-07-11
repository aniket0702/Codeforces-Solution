s = raw_input()
if len(s) == 1:
	if s.isupper():
		print s.lower()
	else:
		print s.upper()
elif s.isupper():
	print s.lower()
elif s[1:].isupper():
	print s[0].upper()+s[1:].lower()
else:
	print s