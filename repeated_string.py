s = 'abcac'
n = 10

s = "a"
n = 1000000000000

s = "aba"
n = 10

s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
n = 549382313570
'''
import math
# s = input()
# n = int(input())
if len(s) == 1 and s == 'a':
  print(n)
else:
  length = len(s)
  times = math.ceil(n/length)
  st = s * times
  subs = st[:n]
  count_a = subs.count('a')
  print(count_a)
'''

s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))