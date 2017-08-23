n = input()
l = list(map(int,raw_input().split()))
# cc = 0
c = 0
for i in l:
    if i%2 == 1:
        c+=1
if c%2 == 1:
    print "First"
else:
    print "Second"
