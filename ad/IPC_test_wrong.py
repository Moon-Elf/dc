from multiprocessing import Process
import os

def test_process():
    print(f"Child process started with PID: {os.getpid()}")

if __name__ == "__main__":
    print(f"Main process PID: {os.getpid()}")
    p = Process(target=test_process)
    p.start()
    p.join()
