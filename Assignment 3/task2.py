class min_heap:
    def __init__(self, arr):
        self.new_arr = [0] * 5
        self.key = 0
        self.arr = arr

    def hasParent(self, index):
        return (index-1) // 2 >= 0

    def hasLeftChild(self, index):
        return 2*index + 1 < self.key

    def hasRightChild(self, index):
        return 2*index + 2 < self.key

    def swap(self, index1, index2):
        self.new_arr[index1], self.new_arr[index2] = self.new_arr[index2] , self.new_arr[index1]
    
    def build(self):
        for i in self.arr:
            self.add(i)

    def add(self, elem):
        self.new_arr[self.key] = elem
        self.key += 1
        self.swimup(self.key - 1)

    def swimup(self, index):
        parent_index = (index-1) // 2
        if (self.hasParent(index) and self.new_arr[parent_index] > self.new_arr[index]):
            self.swap(parent_index, index)
            self.swimup(parent_index)

    def delete(self):
        if self.key == 0:
            return
        elem = self.new_arr[0]
        self.new_arr[0] = self.new_arr[self.key - 1]
        self.key -= 1
        self.sink(0)
        return elem

    def sink(self, index):
        smallest = index
        left_index = 2*index + 1
        right_index = 2*index + 2
        if (self.hasLeftChild(index) and self.new_arr[smallest] > self.new_arr[left_index]):
            smallest = left_index
        if (self.hasRightChild(index) and self.new_arr[smallest] > self.new_arr[right_index]):
            smallest = right_index
        if (smallest != index):
            self.swap(index, smallest)
            self.sink(smallest)
        

    def heapSort(self):
        sorted_array = []
        for i in range(len(self.arr)):
            sorted_array.append(self.delete())
        return sorted_array

input_file = open("input2.txt", "r")
output_file = open("output2.txt", "w")
arr = input_file.readline().strip().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

heap = min_heap(arr)
heap.build()


command = input("Enter 'A' or 'B' or 'S'")
if command == 'B':
    print(str(heap.new_arr), file=output_file)
    print(str(heap.delete()), file=output_file)
    # check if deleted or not
    print(str(heap.new_arr), file=output_file)
elif command == 'S':
    print(str(heap.heapSort()), file=output_file)
elif command == 'A':
    heap.add(int(input("Enter element to be added")))
    print(str(heap.new_arr), file=output_file)

output_file.close()