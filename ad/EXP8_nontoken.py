import time

class LamportClock:
    def __init__(self, pid, max_requests):
        self.pid = pid
        self.clock = 0
        self.replies = 0
        self.requests = []
        self.max_requests = max_requests
        self.request_count = 0

    def increment(self):
        self.clock += 1
        return self.clock

    def request_critical_section(self, processes):
        if self.request_count >= self.max_requests:
            print(f"Process {self.pid} has stopped making requests.")
            return

        self.increment()
        print(f"Process {self.pid} requesting critical section at {self.clock}")
        self.request_count += 1

        for process in processes:
            if process.pid != self.pid:
                process.receive_request(self.pid, self.clock)

    def receive_request(self, sender_pid, sender_clock):
        self.increment()
        print(f"Process {self.pid} received request from {sender_pid} at {self.clock}")
        if self.clock > sender_clock or (self.clock == sender_clock and self.pid > sender_pid):
            self.send_reply(sender_pid)

    def send_reply(self, receiver_pid):
        print(f"Process {self.pid} replying to {receiver_pid}")

    def enter_critical_section(self):
        print(f"Process {self.pid} entering critical section")

    def exit_critical_section(self):
        print(f"Process {self.pid} exiting critical section")


# Simulating the processes
if __name__ == "__main__":
    p0 = LamportClock(0, 1)
    p1 = LamportClock(1, 1)
    p2 = LamportClock(2, 3)

    processes = [p0, p1, p2]

    # Simulating actions
    p2.request_critical_section(processes)
    p1.request_critical_section(processes)
    p2.request_critical_section(processes)
    p0.request_critical_section(processes)
    p2.enter_critical_section()
    p2.exit_critical_section()
