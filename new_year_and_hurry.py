n,k = map(int,raw_input().split())
x = 240-k
cnt=0
for i in range(1,n+1):
	if x-5*i >=0:
		x-=5*i
		cnt+=1
	else:
		break
			
print cnt

