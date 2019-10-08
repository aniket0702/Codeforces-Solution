# N = int(input())
# c = list(map(int, input().split()))

N  = 7
c = "0 0 1 0 0 1 0"

n = 6
c = "0 0 0 1 0 0"
c = list(map(int, c.split()))

'''
i = 0
steps = 0
while i < N-1:
  if i+2<N and c[i+2] == 0 :
    i = i+2
    steps += 1
  else:
    i = i+1
    steps += 1
  
print(steps)
'''


res = 0
i = 0
while i < n-1:
    if i+2<n and c[i+2] == 0:
        i = i+2
        res += 1
    else:
        i = i+1
        res += 1
print(res)