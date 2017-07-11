n = input()
l = list(map(int,raw_input().split()))
li = list(map(int,raw_input().split()))
s = set(l[1:]+li[1:])
if 0 in s:
	s.remove(0)
if len(s) >= n:
	print "I become the guy."
else:
	print "Oh, my keyboard!"