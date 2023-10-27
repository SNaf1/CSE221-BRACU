#task3b
class PatientQueue:
    def __init__(self):
        self.queue = []

    def swim(self, index):
        while index > 0 and self.queue[index][1] < self.queue[(index-1)//2][1]:
            self.queue[index], self.queue[(index-1)//2] = self.queue[(index-1)//2], self.queue[index]
            index = (index-1)//2

    def sink(self, index):
        n = len(self.queue)
        while 2*index+1 < n:
            j = 2*index+1
            if j+1 < n and self.queue[j][1] > self.queue[j+1][1]:
                j += 1
            if self.queue[index][1] <= self.queue[j][1]:
                break
            self.queue[index], self.queue[j] = self.queue[j], self.queue[index]
            index = j

    def enque(self, patient):
        self.queue.append(patient)
        self.swim(len(self.queue)-1)

    def seeDoctor(self):
        if len(self.queue) == 0:
            return None
        patient = self.queue[0][0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.sink(0)
        return patient

    def printQueue(self):
        for patient in self.queue:
            print(patient[0])

patient_queue = PatientQueue()

with open('input3b.txt', 'r') as f:
    lines = f.readlines()

output = open('output3b.txt', 'w')

for line in lines:
    parts = line.strip().split()
    if parts[0] == 'see' and parts[1] == 'doctor':
        patient = patient_queue.seeDoctor()
        if patient is not None:
            output.write(patient + "\n")

    elif parts[1] in ['1', '2', '3']:
        patient_queue.enque((parts[0], parts[1]))
patient_queue.printQueue()
output.close()