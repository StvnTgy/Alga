def nearest_smaller_values(arr):
	n = len(arr)
	result = [0] * n
	stack = []
	
	for i in range(n):
		while stack and arr[stack[-1]] >= arr[i]:
			stack.pop()
		if stack:
			result[i] = stack[-1] + 1
		stack.append(i)
	return result

n = int(input())
szamok = list(map(int, input().split()))

result = nearest_smaller_values(szamok)

print(" ".join(map(str, result)))
