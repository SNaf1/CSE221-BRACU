# task 3
input_file = open("input3.txt", "r")
output_file = open("output3.txt", "w")

n = int(input_file.readline().strip())
list1 = input_file.readline().strip().split()
count = 0
for i in range(n):
    list1[i] = int(list1[i])


def merge(a, b):
    global count
    c = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c += [a[i]]
            i += 1

        else:
            c += [b[j]]
            j += 1
            count += len(a) - i

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    # print(count)
    return c
    

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])

        return merge(a1, a2)

mergeSort(list1)
output_file.write(str(count))
output_file.close()