
class FCFS:
    def __init__(self):
        self.burst = []
        self.arrival = []

        self.n = int(input("Enter the number of processes: "))
        for i in range(self.n):
            self.burst.append(int(input(f"Enter the burst time of process {i+1}: ")))
            self.arrival.append(int(input(f"Enter the arrival time of process {i+1}: ")))

    def findWaitingTime(self):
        self.waiting = [0] * self.n
        total_waiting = self.arrival[0]
        for i in range(self.n):
            self.waiting[i] = total_waiting - self.arrival[i]
            total_waiting += self.burst[i]

    def findTurnAround(self):
        self.turn_around = [0] * self.n
        for i in range(self.n):
            self.turn_around[i] = self.waiting[i] + self.burst[i]

    def findCompletionTime(self):
        self.completion = [0] * self.n
        completion_time = self.arrival[0]
        for i in range(self.n):
            completion_time += self.burst[i]
            self.completion[i] = completion_time

    def printTable(self):
        average_waiting = 0
        average_turn_around = 0
        print("Processes\tBurst Time\tArrival Time\tWaiting Time\tTurn-Around Time\tCompletion Time")
        for i in range(self.n):
            print(f"{i+1}\t\t{self.burst[i]}\t\t{self.arrival[i]}\t\t{self.waiting[i]}\t\t{self.turn_around[i]}\t\t\t{self.completion[i]}")
            average_waiting += self.waiting[i]
            average_turn_around += self.turn_around[i]
        print(f"Average waiting time = {average_waiting/self.n:.5f}")
        print(f"Average turn around time = {average_turn_around/self.n}")

def main():
    fcfs = FCFS()

    fcfs.findWaitingTime()
    fcfs.findTurnAround()
    fcfs.findCompletionTime()
    fcfs.printTable()

if __name__ == "__main__":
    main()