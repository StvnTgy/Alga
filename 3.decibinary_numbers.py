import heapq

def find_dbn(q):
	ind_dict = index_dictionary(q)
	q.sort()
	i = 1
	t = [1]
	db = len(q)
	mem = {}
	#print("q hossza= ",db)
	answer = [0] * db
	cursor = 0
	szum = 1
	
	for a in range(db):
		if q[a] <= 2:
			ind_list = ind_dict.get(q[a])
			for d in ind_list:
				answer[d] = q[a] -1		
			cursor = a + 1
		else:
			break
	
	#print("cursor = ", cursor)
	while cursor < db:
		
		while q[cursor] > szum:
			k = min(i,9)
			#print("k= ",k, "szum= ", szum)
			parity = i % 2
			current = 0
			
			for j in range((k//2)+1):
				#print("for j.., j = ",j)
				index = (i - j*2 - parity) // 2
				current += t[index]
				#print("current= ",current)
			
			t.append(current)
			szum += current
			#print("szum= ", szum, "q[cursor] = ", q[cursor])
			i += 1
			

		if i not in mem:
			dbn_list, mem = get_all_dbn_equal_to(i-1,mem)
		else:
			dbn_list = mem[i]
				
		b = (szum-q[cursor])
		e = heapq.nlargest(b+1,dbn_list)[-1]
		
		ind_list = ind_dict.get(q[cursor])
		for d in ind_list:
			answer[d] = e
		cursor += 1
		
		
		
	return answer
	
def get_all_dbn_equal_to(i, memo = {}):
	if i in memo:
		return memo[i],memo
	s = []
	par = i % 2
	
	for m in range((min(i,9) // 2) + 1):
		p = (i - 2*m - par) // 2
		if p <= 1:
			add = [p]
		else:
			add,memo = get_all_dbn_equal_to(p,{})
		add = [(10*x + 2*m + par) for x in add]
		s.extend(add)
	
	memo[i] = s
	return s, memo

	
def index_dictionary(input_list):
    index_dict = {}
    
    for index, value in enumerate(input_list):

        if value not in index_dict:
            index_dict[value] = [index]
        else:
            index_dict[value].append(index)
    
    return index_dict



n = int(input())
q = []
for i in range(n):
	q.append(int(input()))

c = find_dbn(q)
for cc in c:
	print(cc)
