n = input()
l = []
for i in range(n):
	lt= list(map(int,raw_input().split()))
	l.append(lt)
x=0
y=0
z=0
for i in range(n):
	x+=l[i][0]
	y+=l[i][1]
	z+=l[i][2]
if x == 0 and y==0 and z==0:
	print "YES"
else:
	print "NO"