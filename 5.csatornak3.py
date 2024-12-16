from sys import stdin, stdout
import heapq


v, e, a, b = list(map(int, stdin.readline().split()))
graph = {i: [] for i in range(v)}
for i in range(e):
	u,v,w = list(map(int, stdin.readline().split()))
	if v != a:
		graph[u-1].append((v-1, w))
	if v != b:
		graph[v-1].append((u-1, w))
	
start = a - 1
end = b - 1

priority_queue = [(-1000000, start)]
capacities = {start: 1000000}


while priority_queue:
	current_capacity, current_node = heapq.heappop(priority_queue)
	current_capacity = - current_capacity
		
	for neighbor, capacity in graph[current_node]:
		new_capacity = min(current_capacity, capacity)
		
		if new_capacity > capacities.get(neighbor, 0):
			capacities[neighbor] = new_capacity
			heapq.heappush(priority_queue, (-new_capacity, neighbor))


max_cap = capacities[end]

priority_queue = [(0,start)]
lengths = {start: 0}

while priority_queue:
	current_length, current_node = heapq.heappop(priority_queue)
	
	if current_node == end:
		break
		
	for neighbor, capacity in graph[current_node]:
		if capacity >= max_cap:
			new_length = current_length + 1
			
			if new_length < lengths.get(neighbor, 20000):
				lengths[neighbor] = new_length
				heapq.heappush(priority_queue, (new_length, neighbor))

length = lengths[end]

stdout.write(f"{max_cap}\n")
stdout.write(f"{length}\n")
