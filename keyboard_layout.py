import sys
s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
for i in s3:
	if i.isalpha() == True:
		d = s1.index(i.lower())
		if i.islower()== True:
			sys.stdout.softspace= False
			print s2[d].lower(),
		else:
			sys.stdout.softspace= False
			print s2[d].upper(),
	else:
		sys.stdout.softspace= False
		print i,
		