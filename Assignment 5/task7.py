#task 7
def dfs(node, parent, depth):
    visited[node] = True
    depth[node] = depth[parent] + 1
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node, node, depth)

def get_depth(x):
    return depth[x]

with open("input7.txt", "r") as input_file:
    n = int(input_file.readline().strip())
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input_file.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

visited = [False] * n
depth = [0] * n

dfs(0, -1, depth)
farthest_node = max(range(n), key=get_depth)

visited = [False] * n
depth = [0] * n

dfs(farthest_node, -1, depth)
second_farthest_node = max(range(n), key=get_depth)

with open("output7.txt", "w") as output_file:
    output_file.write(f"{second_farthest_node+1} {farthest_node+1}\n")
