# task 4
with open('input4.txt', 'r') as input_file:
    n, m = map(int, input_file.readline().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u-1].append(v-1)

visited = [False] * n
stack = []
cycle = False

def dfs(node):
    global cycle
    stack.append(node)
    visited[node] = True
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)
        elif visited[adj_node] and adj_node in stack:
            cycle = True

    stack.pop()

dfs(0)

with open('output4.txt', 'w') as output_file:
    if cycle:
        output_file.write('YES')
    else:
        output_file.write('NO')