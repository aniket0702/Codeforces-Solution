n,k = map(int,raw_input().split())
s = raw_input()
l = []
for i in s:
	l.append(i)
lt = n-1
j=0
for i in range(k):
	j=0
	while j < n-1:
		if l[j]=="B" and l[j+1] == "G":
			l[j] = "G" 
			l[j+1] = "B"
			j+=1
			# print j
		j+=1
print "".join(l)