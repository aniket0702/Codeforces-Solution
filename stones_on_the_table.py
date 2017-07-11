n = input()
s= raw_input()
r = []
cnt =0
c = 0
r.append(s[0])
for i in range(1,n):
	if s[i] == r[c]:
		cnt+=1
	else:
		c+=1
		r.append(s[i])
print cnt