n = input()
l = list(map(int,raw_input().split()))
# l = sorted(l)
cnt = 0
s = 0
lt = [0,0,0,0]
for i in l:
	lt[i-1]+=1
# print lt
cnt = lt[3]
cnt +=lt[2]
lt[0]-=lt[2]
cnt+=(lt[1]/2)
lt[1] %=2
# print cnt

if lt[1]:
	cnt+=1
	lt[0]-=2
if lt[0]>0:
	cnt+= (lt[0]/4)
	lt[0] %=4
if lt[0]>0:
	cnt+=1
print cnt
