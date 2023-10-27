#task3
from queue import PriorityQueue

with open("input3.txt", "r") as f:
    n, m = map(int, f.readline().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, w = map(int, f.readline().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        u = pq.get()[1]
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v]:
                alt = max(dist[u], weight)
                if alt < dist[v]:
                    dist[v] = alt
                    pq.put((dist[v], v))

    return dist

dist = dijkstra(graph, 0)
with open('output3.txt', 'w') as output_file:
    if dist[n-1] == float('inf'):
        output_file.write("Impossible")
    else:
        output_file.write(f"{dist[n-1]}")