def find_course_order(n, m, dep_list):
	queue = deque([i for i in range(n) if no_of_deps[i] == 0])
	course_order = []
	
	while queue:
		current = queue.popleft()
		course_order.append(current+1)
		for neighbor in dep_list[current]:
			no_of_deps[neighbor] -= 1
			if no_of_deps[neighbor] == 0:
				queue.append(neighbor)
				
	if len(course_order) == n:
		return course_order
	else:
		return "IMPOSSIBLE"

from collections import deque
n, m = map(int, input().split())

dependencies = []

dep_list = []
#l_fs = defaultdict(list)

for i in range(n):
	dep_list.append([])

no_of_deps = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    dep_list[a-1].append(b-1)
    no_of_deps[b-1] += 1
    
#for _ in range(m):
#    a, b = map(int, input().split())
#    dependencies.append((a,b))
    

result = find_course_order(n, m, dep_list)


if result == "IMPOSSIBLE":
    print(result)
else:
    print(" ".join(map(str, result)))




