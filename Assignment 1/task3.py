def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_file = open("input3.txt", "r")
n = int(input_file.readline().strip())
arr = [0] * n
elements = input_file.readline().strip().split()

for i in range(n):
    arr[i] = int(elements[i])

input_file.close()

sorted_arr = insertionSort(arr)

output_file = open("output3.txt", "w")

for x in sorted_arr:
    output_file.write(str(x) + " ")

output_file.close()
  
# In the best-case scenario, when the array is already sorted, Insertion Sort will make n-1 comparisons, resulting in a time complexity of θ(n). 
# This is because each element will be inserted in its correct place in the already sorted subarray, with no swaps required.