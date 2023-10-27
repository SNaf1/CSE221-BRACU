file1 = open('input1a.txt', mode = 'r')
output = open('output1a.txt', mode = 'w')
int1 = int(file1.readline())

for i in range(int1):
    temp1 = int(file1.readline())
    if temp1 % 2 == 0:
        print(f"{temp1} is a an Even number.", file = output)
    else:
        print(f"{temp1} is a an Odd number.", file = output)

output.close()