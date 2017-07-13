n = raw_input()
l = 0
u = 0
for i in n:
	if i.islower() == True:
		l+=1
	else:
		u+=1
if l>=u:
	print n.lower()
else:
	print n.upper()