#task 3
with open('input3.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, f.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

visited = [False] * n
path = []

def dfs(node, path):
    visited[node] = True
    path.append(node+1)
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node, path)
    

dfs(0, path)

with open('output3.txt', 'w') as f:
    f.write(' '.join(map(str, path)))