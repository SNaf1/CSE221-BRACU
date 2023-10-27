# task 1a
input_file = open("input1a_1.txt", "r")
output = open("output1a_1.txt", mode = 'w')
arr = input_file.readline().strip().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

N, S = arr[0], arr[1]

elements = input_file.readline().strip().split()


for i in range(N):
    elements[i] = int(elements[i])

found = False
for i in range(len(elements)):
    if found == True:
        break
    for j in range(i+1, len(elements)):
        if elements[i] + elements[j] == S:
            index1 = i + 1
            index2 = j + 1
            found = True
            break

if found == True:
    print(f"{index1} {index2}", file = output)
else:
    print(f"IMPOSSIBLE", file = output)

output.close()