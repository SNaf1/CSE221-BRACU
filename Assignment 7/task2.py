#task 2
from queue import PriorityQueue

input_file = open('input2.txt', 'r')
N, M = map(int,input_file.readline().split())

pq = PriorityQueue()
for i in range(M):
  pq.put(0)

tasks = [tuple(map(int, input_file.readline().split())) for i in range(N)]
sorted_tasks = sorted(tasks, key=lambda x: x[0])

count = 0

for i in range(len(sorted_tasks)):
  if pq.queue[0]<=sorted_tasks[i][0]:
    pq.get()
    count += 1
    pq.put(sorted_tasks[i][1])

  elif pq.queue[0] >= sorted_tasks[i][1]:
    pq.get()
    pq.put(sorted_tasks[i][1])

with open('output2.txt', 'w') as output_file:
    output_file.write(str(count))