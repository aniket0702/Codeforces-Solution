n= input()
cnt=0
while n:
	x,y= map(int,raw_input().split())
	if y-x>=2:
		cnt+=1
	n-=1
print cnt