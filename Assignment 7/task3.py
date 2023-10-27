#Task 3
input_file = open('input3.txt', 'r')
output_file = open('output3.txt', 'w')

N,M = map(int,input_file.readline().split())

root = [0] * (N+1)
count = [1] * (N+1)

for i in range(N+1):
    root[i] = i

for i in range(M):
    r,f = map(int,input_file.readline().split())

    if root[r] != root[f]:
      count[root[r]] = count[root[r]] + count[root[f]]
      count[root[f]] = count[root[r]]
      output_file.write(str(count[root[f]]) + '\n')
      root[f] = root[r]

    else:
      output_file.write(str(count[root[f]]) + '\n')

output_file.close()