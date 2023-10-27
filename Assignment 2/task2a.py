# Task 2a
def merge(a, b):
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
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

input_file = open("input2a_1.txt", "r")

N = int(input_file.readline().strip())


list1 = input_file.readline().strip().split()

for i in range(N):
    list1[i] = int(list1[i])

M = int(input_file.readline().strip())

list2 = input_file.readline().strip().split()

for i in range(M):
    list2[i] = int(list2[i])

new_arr = list1 + list2

arr_sorted = mergeSort(new_arr)

output = open('output2a_1.txt', 'w')
output.write(' '.join(str(x) for x in arr_sorted))
output.close()