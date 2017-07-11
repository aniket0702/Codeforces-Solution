s= raw_input()
n = len(s)
fl =0
c = "hello"
cnt = 0
for i in range(n):
	if s[i] == c[cnt]:
		cnt+=1
	if cnt == 5:
		fl = 1
		break
if fl:
	print "YES"
else:
	print "NO"