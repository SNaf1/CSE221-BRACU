# task 2b
input_file = open("input2b_1.txt", "r")
output = open("output2b_1.txt", mode = 'w')
N = int(input_file.readline().strip())


list1 = input_file.readline().strip().split()

for i in range(N):
    list1[i] = int(list1[i])

M = int(input_file.readline().strip())

list2 = input_file.readline().strip().split()

for i in range(M):
    list2[i] = int(list2[i])


new_arr = [0] * (N + M)

i = 0
j = 0

index = 0
while i < N and j < M:
    if list1[i] < list2[j]:
        new_arr[index] = list1[i]
        i += 1
    else:
        new_arr[index] = list2[j]
        j += 1

    index += 1


if i < N:
    for k in range(i, N):
        new_arr[index] = list1[k]
        index += 1
elif j < M:
    for k in range(j, M):
        new_arr[index] = list2[k]
        index += 1

for x in new_arr:
    output.write(str(x) + " ")

output.close()