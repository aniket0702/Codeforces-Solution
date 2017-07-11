n = raw_input()
l=[]
for i in n[::2]:
	l.append((i))
l = sorted(l)
print "+".join(l)