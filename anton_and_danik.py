n = input()
c1=0
c2=0
s= raw_input()
for i in s:
	if i == "A":
		c1+=1
	else:
		c2+=1
if c1>c2:
	print "Anton"
elif c2 > c1:
	print "Danik"
else:
	print "Friendship"