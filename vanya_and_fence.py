n,k = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
w = 0
for i in l:
	if i<= k:
		w+=1
	else:
		w+=2
print w