n=input()
l = list(map(int,raw_input().split()))
l = sorted(l)
s = 0
c = 0
cnt =0
for i in l:
	s+=i
for i in l[::-1]:
	c+=i
	cnt+=1
	if c >(s/2):
		break
print cnt 