#task 5
with open("input5.txt", "r") as input_file:
    n, m, D = map(int, input_file.readline().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)


visited = [False] * len(graph)
queue = [(0, [])]
visited[0] = True
path_found = False

while queue:
    node, path = queue.pop(0)
    if node == D-1:
        path_found = True
        break

    for adj_node in graph[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            queue.append((adj_node, path+[node+1]))

with open("output5.txt", "w") as output_file:
    if path_found:
        output_file.write("Time: {}\n".format(len(path)))
        output_file.write("Shortest Path: {}\n".format(" ".join(map(str, path+[D]))))
    else:
        output_file.write("Can't reach\n")
