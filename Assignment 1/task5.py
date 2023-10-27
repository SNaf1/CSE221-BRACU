def sort_trains(name, place, time):
    n = len(name)
    for i in range(n):
        for j in range(0, n - i - 1):
            if name[j] > name[j + 1]:
                name[j], name[j + 1] = name[j + 1], name[j]
                place[j], place[j + 1] = place[j + 1], place[j]
                time[j], time[j + 1] = time[j + 1], time[j]
            elif name[j] == name[j + 1]:
                departure_time_j = time[j]
                departure_time_j_plus_1 = time[j + 1]
                if departure_time_j < departure_time_j_plus_1:
                    name[j], name[j + 1] = name[j + 1], name[j]
                    place[j], place[j + 1] = place[j + 1], place[j]
                    time[j], time[j + 1] = time[j + 1], time[j]
    return name, place, time

input_file = open("input5.txt", "r")
n = int((input_file.readline().strip()))

name = [None] * n
place = [None] * n
time = [None] * n

for i in range(n):
    lines = input_file.readline().strip().split()
    name[i] = lines[0]
    place[i] = lines[4]
    time[i] = int(lines[6].replace(":", ""))

sorted_name, sorted_place, sorted_times = sort_trains(name, place, time)

output_file = open("output5.txt", "w")
for i in range(n):
        hour = str(sorted_times[i] // 100)
        minute = str(sorted_times[i] % 100)
        if len(hour) == 1:
            hour = '0' + hour
        if len(minute) == 1:
            minute = '0' + minute
        output_file.write(f"{sorted_name[i]} will departure for {sorted_place[i]} at {hour}:{minute}\n")
        
output_file.close()