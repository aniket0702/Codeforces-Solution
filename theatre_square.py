from math import ceil
x,y,z = map(float,raw_input().split())
s = ceil(x/z)*ceil(y/z)
print int(s)
