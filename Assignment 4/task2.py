# task 2
input_file = open("input2.txt", "r")
output_file = open("output2.txt", "w")

n = int(input_file.readline().strip())
list1 = input_file.readline().strip().split()
max_val = None
for i in range(n):
    list1[i] = int(list1[i])

def merge(a, b):
    c = []
    i = 0
    j = 0


    while i < len(a) and j < len(b):
        global max_val
        temp_max = None
        if a[i] < b[j]:
            c += [a[i]]
            i += 1
            if max_val == None:
                max_val = b[j]
                temp_max = max_val
            else:
                temp_max = b[j]
                if temp_max > max_val:
                    max_val = temp_max
        else:
            c += [b[j]]
            j += 1
            if max_val == None:
                max_val = a[i]
                temp_max = max_val
            else:
                temp_max = a[i]
                if temp_max > max_val:
                    max_val = temp_max


    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    
    return c
    

def mergeSort(arr):
    if len(arr) <= 1:
        global max_val
        max_val = arr[0]
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])

        return merge(a1, a2)

mergeSort(list1)
output_file.write(str(max_val))

output_file.close()