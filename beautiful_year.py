x = input()
for i in range(x+1,9013): 
	# l = []
	st= set()
	s = str(i)
	for j in s:
		st.add(int(j))
	if len(st) == 4:
		print i
		break