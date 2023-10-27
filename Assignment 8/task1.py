#task 1
input_file = open('input1.txt', 'r')
N, M = map(int, input_file.readline().split())

parent = list(range(N))
rank = [0] * N

arr1 = []
for i in range(M):
    u, v, w = map(int, input_file.readline().split())
    arr1.append((w, u - 1, v - 1))

arr1.sort()

cost = 0

for w, u, v in arr1:
    x, y = u, v
    
    while parent[x] != x:
        x = parent[x]
    while parent[y] != y:
        y = parent[y]

    if x != y:
        if rank[x] > rank[y]:
            x, y = y, x
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
        cost += w

with open('output1.txt', 'w') as output_file:
    output_file.write(str(cost))