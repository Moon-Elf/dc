import logging
import os
import time
from multiprocessing import Process, Array

# Set up logging at the top
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

def process1(shared):
    process1_logger = logging.getLogger('process1')
    process1_logger.info(f"Pid: {os.getpid()}")
    for i in range(1, 11):
        while True:
            try:
                process1_logger.info(f"Writing {int(i)}")
                shared[i - 1] = i
                if i % 6 == 0:
                    process1_logger.info("Intentionally sleeping for 5 seconds")
                    time.sleep(5)
                break
            except Exception as e:
                print(str(e))
                pass
    process1_logger.info("Finished process 1")

def process2(shared):
    process2_logger = logging.getLogger('process2')
    process2_logger.info(f"Pid: {os.getpid()}")
    for i in range(10):
        while True:
            try:
                line = shared[i]
                if line == -1:
                    process2_logger.info("Data not available, sleeping for 1 second before retrying")
                    time.sleep(1)
                    raise Exception('pending')
                process2_logger.info(f"Read: {int(line)}")
                break
            except Exception:
                pass
    process2_logger.info("Finished process 2")

def main():
    parent_logger = logging.getLogger('parent')
    parent_logger.info(f"Pid: {os.getpid()}")

    arr = Array('i', [-1] * 10)
    procs = [
        Process(target=process1, args=(arr,)),
        Process(target=process2, args=(arr,))
    ]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

if __name__ == '__main__':
    main()
