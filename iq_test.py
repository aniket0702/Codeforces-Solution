n = input()
l = list(map(int,raw_input().split()))
ce=0
co= 0
lo= 0
le= 0
for i in range(n):
	if l[i]%2 == 0:
		ce+=1
		le =i
	else:
		co+=1
		lo =i

if ce==1:
	print le+1
else:
	print lo+1	