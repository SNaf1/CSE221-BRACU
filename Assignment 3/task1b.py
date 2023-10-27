input_file = open("input1b.txt", "r")
output_file = open('output1b.txt', 'w')
arr = input_file.readline().strip().split()
k = int(input_file.readline())

for i in range(len(arr)):
    arr[i] = int(arr[i])

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
            # return arr[pi]
            output_file.write(str(arr[pi]))
            return

        elif pi > k - 1:
            high = pi - 1
            
        else:
            low = pi + 1

findK(arr, k)
output_file.close()