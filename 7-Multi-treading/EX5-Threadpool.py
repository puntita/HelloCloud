import logging
import threading
import time
import concurrent.futures

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ =="__main__":
    foemat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        dafefmt="%H:%M:%S")

    with concurrent.fututes.ThreadPoolexecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))