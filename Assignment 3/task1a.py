#task 1a
input_file = open("input1a.txt", "r")
output_file = open('output1a.txt', 'w')
arr = input_file.readline().strip().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)  
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    # pivot (Element to be placed at right position)
    pivot = arr[high]
    i = low-1  # Index of smaller element and indicates the right position of pivot found so far
    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i = i+1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def findK(arr, k):
    low = 0
    high = len(arr) - 1

    while True:
        pi = partition(arr, low, high)

        if pi == k - 1:
            return arr[pi]

        elif pi > k - 1:
            high = pi - 1
            
        else:
            low = pi + 1

low = 0
high = len(arr) - 1
quickSort(arr, low, high)

for i in arr:
    output_file.write(str(i) + " ")
    
output_file.close()