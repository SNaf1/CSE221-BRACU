#task3a
class PatientQueue:
    def __init__(self):
        self.queue = []

    def enque(self, name, priority):
        self.queue.append((name, priority))
        n = len(self.queue)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.queue[j][1] > self.queue[j+1][1]:
                    self.queue[j], self.queue[j+1] = self.queue[j+1], self.queue[j]

    def seeDoctor(self):
        if len(self.queue) == 0:
            return None
        for i in range(1, 4):
            for j in range(len(self.queue)):
                if self.queue[j][1] == i:
                    return self.queue.pop(j)[0]

    def printQueue(self):
        for patient in self.queue:
            print(patient[0])

patient_queue = PatientQueue()
with open('input3a.txt', 'r') as f:
    lines = f.readlines()

output = open('output3a.txt', 'w')

for line in lines:
    parts = line.strip().split()
    if parts[0] == 'see' and parts[1] == 'doctor':
        patient = patient_queue.seeDoctor()
        if patient is not None:
            output.write(patient + "\n")
    elif parts[1] in ['1', '2', '3']:
        patient_queue.enque(parts[0], int(parts[1]))
patient_queue.printQueue()
output.close()