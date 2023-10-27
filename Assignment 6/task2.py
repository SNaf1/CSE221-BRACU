#task 2
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

with open('input2.txt', 'r') as input_file:
    n, m = map(int, input_file.readline().split())
    adj_list = [[] for i in range(n)]
    for i in range(m):
        u, v, w = map(int, input_file.readline().split())
        adj_list[u-1].append((v-1, w))
    source1, source2 = map(int, input_file.readline().split())
    

dist1 = dijkstra(adj_list, source1-1, n)
dist2 = dijkstra(adj_list, source2-1, n)


dist3 = []
for i in range(len(dist1)):
    if dist1[i] != -1 and dist2[i] != -1:
        if dist1[i] >= dist2[i]:
            dist3.append(dist1[i])
        else:
            dist3.append(dist2[i])


with open('output2.txt', 'w') as output_file:
    if len(dist3) != 0:
        output_file.write(f"Time {min(dist3)}\n")
        for i in range(len(dist1)):
            if dist1[i] == min(dist3) or dist2[i] == min(dist3):
                output_file.write(f"Node {i+1}")
                break
    else:
        output_file.write("Impossible")