def numret(c):
	return int(ord(c)-65)


l = [0] *26
n = raw_input()
for i in n:
	l[numret(i)]+=1
n = raw_input()
for i in n:
	l[numret(i)]+=1
n = raw_input()
for i in n:
	l[numret(i)]-=1
fl =0
for i in l:
	if i != 0:
		fl=1
		break
if fl:
	print "NO"
else:
	print "YES"
