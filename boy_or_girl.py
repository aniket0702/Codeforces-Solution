s = raw_input()
l = [0]*26
cnt= 0
for i in s:
	x = ord(i)-97
	if l[x] == 0:
		l[x] = 1
		cnt+=1
if cnt%2 == 0:
	print "CHAT WITH HER!"
else:
	print "IGNORE HIM!"