import threading
import time

def process(iterable):
    for letter in iterable:
        print(letter)
        time.sleep(0.2)


t1 = threading.Thread(target=process, args=("helloworld",))
t2 = threading.Thread(target=process, args=(range(10),))

t1.start(), t2.start()

t1.join(), t2.join()

