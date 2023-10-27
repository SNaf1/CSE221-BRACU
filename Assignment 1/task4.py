def selection_sort(n, id, marks):
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if marks[j] > marks[max_index] or (marks[j] == marks[max_index] and id[j] < id[max_index]):
                max_index = j

        id[i], id[max_index] = id[max_index], id[i]
        marks[i], marks[max_index] = marks[max_index], marks[i]
    return (id, marks)

input_file = open("input4.txt", "r")
n = int(input_file.readline().strip())
id = [0] * n
marks = [0] * n
id_list = input_file.readline().strip().split()
marks_list = input_file.readline().strip().split()

for i in range(n):
    id[i] = int(id_list[i])
    marks[i] = int(marks_list[i])
input_file.close()

sorted_id, sorted_marks = selection_sort(n, id, marks)

output_file = open("output4.txt", "w")

for i in range(n):
    output_file.write(f"ID: {sorted_id[i]} Mark: {sorted_marks[i]}\n")
    
output_file.close()