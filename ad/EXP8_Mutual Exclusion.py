import threading
import time

class MultiTokenMutex:
    def __init__(self, num_processes, num_tokens):
        self.num_processes = num_processes
        self.num_tokens = num_tokens
        self.tokens = [False] * num_processes  # Tracks which processes have a token
        self.lock = threading.Lock()

    def request_token(self, process_id):
        with self.lock:
            if self.tokens[process_id]:
                print(f"Process {process_id} already has a token.")
                return True
            if self.num_tokens > 0:
                self.tokens[process_id] = True
                self.num_tokens -= 1
                print(f"Process {process_id} got a token.")
                return True
            else:
                print(f"Process {process_id} waiting for a token.")
                return False

    def release_token(self, process_id):
        with self.lock:
            if self.tokens[process_id]:
                self.tokens[process_id] = False
                self.num_tokens += 1
                print(f"Process {process_id} released the token.")
            else:
                print(f"Process {process_id} doesn't have a token to release.")

    def enter_critical_section(self, process_id):
        print(f"Process {process_id} entering critical section.")
        # Simulate work in the critical section
        time.sleep(0.1)
        print(f"Process {process_id} exiting critical section.")

    def run_process(self, process_id):
        if self.request_token(process_id):
            self.enter_critical_section(process_id)
            self.release_token(process_id)
        else:
            time.sleep(0.1)
            self.run_process(process_id)  # Retry if no token is available

# Simulating the processes with multi-token mutual exclusion
if __name__ == "__main__":
    num_processes = 5
    num_tokens = 2  # Limiting the number of tokens in the system
    mutex = MultiTokenMutex(num_processes, num_tokens)

    threads = []
    for i in range(num_processes):
        t = threading.Thread(target=mutex.run_process, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
