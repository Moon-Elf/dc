import logging
import os
import time
from multiprocessing import Process, Array

def process1(shared):
    logger = logging.getLogger('process1')
    logger.info(f"Pid: {os.getpid()}")
    for i in range(1, 11):
        while True:
            try:
                logger.info(f"Writing {i}")
                shared[i - 1] = i
                if i % 6 == 0:
                    logger.info("Intentionally sleeping for 5 seconds")
                    time.sleep(5)
                break
            except Exception as e:
                logger.error(str(e))
                pass
    logger.info("Finished process 1")

def process2(shared):
    logger = logging.getLogger('process2')
    logger.info(f"Pid: {os.getpid()}")
    for i in range(10):
        while True:
            try:
                line = shared[i]
                if line == -1:
                    logger.info("Data not available, sleeping for 1 second before retrying")
                    time.sleep(1)
                    raise Exception("pending")
                logger.info(f"Read: {line}")
                break
            except Exception:
                pass
    logger.info("Finished process 2")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] [%(name)s]: %(message)s'
    )

if __name__ == '__main__':
    setup_logging()

    logger = logging.getLogger('parent')
    logger.info(f"Pid: {os.getpid()}")

    arr = Array('i', [-1] * 10)

    p1 = Process(target=process1, args=(arr,))
    p2 = Process(target=process2, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
