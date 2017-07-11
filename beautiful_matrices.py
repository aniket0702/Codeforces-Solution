l = []
for i in range(5):
	lt = list(map(int,raw_input().split()))
	l.append(lt)
x =0
y= 0
for i in range(5):
	for j in range(5):
		if l[i][j] == 1:
			x = i
			y = j
			break

print abs(2-x) + abs(2-y)
