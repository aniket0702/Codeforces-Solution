n = raw_input()
n = str(n)
cnt = 1
fl =0
for i in range(1,len(n)):
	if n[i]== n[i-1]:
		cnt +=1
		if cnt >= 7:
			fl =1
			print "YES"
			break
	else:
		cnt =1
if fl is 0:
	print "NO"