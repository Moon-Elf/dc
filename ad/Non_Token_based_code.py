import heapq

class Message:
    def __init__(self, timestamp, sender_id):
        self.timestamp = timestamp
        self.sender_id = sender_id

    def __lt__(self, other):
        if self.timestamp == other.timestamp:
            return self.sender_id < other.sender_id
        return self.timestamp < other.timestamp

class Process:
    def __init__(self, pid, all_pids):
        self.pid = pid
        self.clock = 0
        self.queue = []
        self.all_pids = all_pids
        self.reply_count = 0

    def send_request(self, processes):
        self.clock += 1
        request = Message(self.clock, self.pid)
        heapq.heappush(self.queue, request)
        print(f"Process {self.pid} requesting critical section at {self.clock}")
        for p in processes:
            if p.pid != self.pid:
                p.receive_request(Message(self.clock, self.pid))

    def receive_request(self, msg):
        self.clock = max(self.clock, msg.timestamp) + 1
        heapq.heappush(self.queue, msg)
        print(f"Process {self.pid} received request from {msg.sender_id} at {msg.timestamp}")

    def send_reply(self, to_pid):
        print(f"Process {self.pid} replying to {to_pid}")

    def check_critical_section(self):
        return self.queue[0].sender_id == self.pid

    def enter_critical_section(self):
        print(f"Process {self.pid} entering critical section")

    def exit_critical_section(self, processes):
        print(f"Process {self.pid} exiting critical section")
        heapq.heappop(self.queue)
        for p in processes:
            if p.pid != self.pid:
                p.receive_release(self.pid)

    def receive_release(self, sender_id):
        self.queue = [msg for msg in self.queue if msg.sender_id != sender_id]
        heapq.heapify(self.queue)

def simulate_lamport():
    # 🔧 Editable Process IDs
    process_ids = [10, 20, 30]  # You can change these to any unique integers
    processes = [Process(pid, process_ids) for pid in process_ids]
    pid_map = {p.pid: p for p in processes}

    # Simulate request and replies
    pid_map[30].send_request(processes)   # Process 30
    pid_map[20].send_request(processes)   # Process 20
    pid_map[30].send_reply(20)

    pid_map[30].send_request(processes)   # Process 30 again
    pid_map[10].send_request(processes)   # Process 10

    pid_map[20].send_reply(10)
    pid_map[30].send_reply(10)

    # Check and enter critical section
    if pid_map[30].check_critical_section():
        pid_map[30].enter_critical_section()
        pid_map[30].exit_critical_section(processes)

if __name__ == "__main__":
    simulate_lamport()
