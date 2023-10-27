# task 1a
input_file = open('input1a.txt', 'r')
output_file = open('output1a.txt', 'w')

n, m = map(int, input_file.readline().split())
adj_matrix = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    u, v, w = map(int, input_file.readline().split())
    adj_matrix[u][v] = w

for i in range(n+1):
    for j in range(n+1):
        output_file.write(str(adj_matrix[i][j]) + ' ')
    output_file.write('\n')

input_file.close()
output_file.close()