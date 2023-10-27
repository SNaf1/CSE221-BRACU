#task 1b
input_file = open("input1b_1.txt", "r")
output = open("output1b_1.txt", mode = 'w')
arr = input_file.readline().strip().split()


for i in range(len(arr)):
    arr[i] = int(arr[i])

N, S = arr[0], arr[1]

elements = input_file.readline().strip().split()

for i in range(N):
    elements[i] = int(elements[i])

dict1 = {}

found = False

for i in range(N):
    try:
        dict1[S - elements[i]]
        found = True
        break
        
    except:
        dict1[elements[i]] = i + 1
        

if found == True:
    print(f"{dict1[S-elements[i]]} {i+1}", file = output)
else:
    print(f"IMPOSSIBLE", file = output)

output.close()