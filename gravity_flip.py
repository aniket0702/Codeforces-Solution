n = input()
l = list(map(int,raw_input().split()))
l = sorted(l)
print " ".join(str(x) for x in l)
