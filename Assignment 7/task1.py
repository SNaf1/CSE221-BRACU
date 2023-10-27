#task1
with open('input1.txt', 'r') as f:
    n = int(f.readline())
    tasks = [tuple(map(int, f.readline().split())) for i in range(n)]

def find_maximum_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    selected_tasks = []
    end_times = []

    for task in sorted_tasks:
        if not selected_tasks or task[0] >= end_times[-1]:
            selected_tasks.append(task)
            end_times.append(task[1])

    return selected_tasks

selected_tasks = find_maximum_tasks(tasks)
k = len(selected_tasks)

with open('output1.txt', 'w') as f:
    f.write(str(k) + '\n')
    for task in selected_tasks:
        f.write('{} {}\n'.format(task[0], task[1]))