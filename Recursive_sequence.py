from collections import deque

def kiszamol(k,b,c,n):
	if n <= k:
		return b[n-1] % MOD
	for i in range(k,n):
		b = recursion(b,c)
	return b[k-1]

def recursion(b,c):
	s = 0
	for i in range(len(b)):
		s = (s + b[i] * c[k-1-i]) % MOD
	b.append(s)
	#print("most ez a bé: ",b)
	b.popleft()
	#print("most ez a bé: ",b)
	return b

MOD = 10**9
out = []
c = int(input())
for _ in range(c):
	k = int(input())
	b = list(map(int, input().split()))
	b = deque(b)
	c = list(map(int, input().split()))
	n = int(input())
	
	result = kiszamol(k,b,c,n)
	out.append(result)

for o in out:
	print(o)
