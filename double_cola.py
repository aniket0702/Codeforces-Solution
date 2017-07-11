n = input()
l= ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r =1
while r*5 < n:
	n-=r*5
	r*=2
print l[(n-1)/r]