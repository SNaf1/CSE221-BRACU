# task 2
with open("input2.txt", "r") as input_file:
    n, m = map(int, input_file.readline().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    path = []

    while queue:
        node = queue.pop(0)
        path.append(node+1)
        for adj_node in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                queue.append(adj_node)

    return path

path = bfs(graph, 0)

with open("output2.txt", "w") as output_file:
    output_file.write(" ".join(map(str, path)))