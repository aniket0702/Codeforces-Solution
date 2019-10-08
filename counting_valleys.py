N = int(input())
s = list(input())
updown = 0
valley = 0
for step in s:
  if step == 'U':
    updown += 1
  else:
    updown -= 1
  if updown == 0 and step == "U":
    valley += 1

print(valley)