import multiprocessing
from datetime import datetime 
from time import sleep 
import random

def now_sleep(seconds): 
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
    sleep(seconds) 
    print("Finished Process!")

if __name__ == '__main__':
    for n in range(3): 
        print("starting processes")
        seconds = random.randint(1, 10) 
        print(f"Process {n} will sleep for {seconds}")
        proc = multiprocessing.Process(target=now_sleep, args=(seconds,)) 
        proc.start()
        