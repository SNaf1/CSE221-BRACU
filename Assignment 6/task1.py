#task 1
from queue import PriorityQueue

def dijkstra(adj_list, source, n):
    dist = [-1] * n
    dist[source] = 0
    pq = PriorityQueue()
    pq.put((0, source))
    while not pq.empty():
        u_distance, u = pq.get()
        
        if u_distance > dist[u]:
            continue

        for v, w in adj_list[u]:
            if dist[v] < 0 or dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))
    return dist

with open('input1.txt', 'r') as input_file:
    n, m = map(int, input_file.readline().split())
    adj_list = [[] for i in range(n)]

    for i in range(m):
        u, v, w = map(int, input_file.readline().split())
        adj_list[u-1].append((v-1, w))
    source = int(input_file.readline().strip())

dist = dijkstra(adj_list, source-1, n)

with open('output1.txt', 'w') as output_file:
    output_file.write(' '.join(str(i) for i in dist))