import array
arr = [1,2,3,4,5,6,7]
print(arr)
d = 2
n = len(arr)
print(n)
for i in range(d):
	temp = arr[0]
	for j in range(n-1):
		arr[j] = arr[j+1]
	arr[n-1] = temp

print(arr)