s = raw_input()
fl =0
for i in s:
	if i=="H" or i == "Q" or i == "9":
		fl =1	
		print "YES"
		break
if fl ==0:
	print "NO"