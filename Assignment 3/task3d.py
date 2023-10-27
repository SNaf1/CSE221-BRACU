import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Initialize empty lists to store input sizes and corresponding times
input_sizes = []
times = []
heap_sort_times = []

# Set the maximum input size to test
max_input_size = 10000

# Test bubble sort with different input sizes and record the time taken
for i in range(1, max_input_size+1, 1000):
    input_sizes.append(i)
    arr = [random.randint(1, 100) for _ in range(i)]
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    times.append(end_time - start_time)

    start = time.time()
    heap_sort(arr)
    end = time.time()
    heap_sort_times.append(end - start)

# Plot the graph
plt.plot(input_sizes, times, label="Bubble Sort")
plt.plot(input_sizes, heap_sort_times, label="Heap Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title("Comparing Time Complexity of Bubble and Heap Sort")
plt.legend()
plt.show()