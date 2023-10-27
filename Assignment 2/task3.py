# Task 3
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

f = open('input3_1.txt', 'r')
n = int(f.readline().strip())
arr1 = [int(x) for x in f.readline().strip().split()]
f.close()


arr_sorted = mergeSort(arr1)

output = open('output3_1.txt', 'w')
output.write(' '.join(str(x) for x in arr_sorted))
output.close()