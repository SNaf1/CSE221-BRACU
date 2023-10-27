#task 1b
input_file = open('input1b.txt', 'r')
output_file = open('output1b.txt', 'w')

dict1 = {}
n, m = map(int, input_file.readline().split())
for i in range(n+1):
    dict1[i] = []

for i in range(m):
    u, v, w = map(int, input_file.readline().split())
    dict1[u].append((v,w))
    
print(dict1)
for key, val in dict1.items():
    output_file.write(str(key) + ' : ')
    for i in val:
        output_file.write(str(i) + ' ')

    output_file.write('\n')
    
input_file.close()
output_file.close()