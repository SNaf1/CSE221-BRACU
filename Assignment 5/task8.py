# task 8
def mark_nodes(adj_list, start, monster_type):
    queue = []
    queue.append(start)
    monster_type[start] = 0
    front = 0
    
    while front < len(queue):
        curr_node = queue[front]
        front += 1
        for neighbor in adj_list[curr_node]:
            if monster_type[neighbor] == -1:
                monster_type[neighbor] = 1 - monster_type[curr_node]
                queue.append(neighbor)
            elif monster_type[neighbor] == monster_type[curr_node]:
                return False
    
    return True

t = int(input())

for case in range(1, t+1):
    n = int(input())
    adj_list = [[] for _ in range(20001)]
    for _ in range(n):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    monster_type = [-1] * 20001
    
    vampires = 0
    lykans = 0
    for i in range(1, 20001):
        if monster_type[i] == -1:
            if mark_nodes(adj_list, i, monster_type):
                if monster_type[i] == 0:
                    vampires += 1
                else:
                    lykans += 1
            else:
                break
    
    print("Case {}: {}".format(case, (20000 - max(vampires, lykans))))
