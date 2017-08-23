def primes(n): # simple Sieve of Eratosthenes 
   odds = range(3, n+1, 2)
   sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
   return len([p for p in odds if p not in sieve])+1

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

n = input()
l = list(map(int,raw_input().split()))
# print primeno(10)
l1=[]
for i in l:	
	x= primes(i)
	l1.append(x)
# print l
# print l1
q= input()
for i in range(q):
	lt,r,k = map(int,raw_input().split())
	s= 0
	for i in range(lt-1,r):
		# print  gcd(l[i],l1[i])
		if gcd(l[i],l1[i]) > k:
			s+=l[i]
	print s