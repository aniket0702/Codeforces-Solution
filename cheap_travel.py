import math
import numpy
n,m,a,b = map(int ,raw_input().split())
s1 = 0
s1+= (n/m)*b
s1+= (n%m)*a
s2 = int((math.ceil(float(n)/m) )*b)	
s3 = n*a
print min(s1,s2,s3)
