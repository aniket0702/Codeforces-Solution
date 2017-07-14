n= input()
l = list(map(int,raw_input().split()))
i=0
fl =0
while  i<n-1 and l[i]<l[i+1] :
	i+=1
while  i<n-1 and l[i]==l[i+1] :
	i+=1
	fl =1
while  i<n-1 and l[i]>l[i+1] :
	i+=1
if  i == n-1:
	print "YES"
else:
	print "NO"