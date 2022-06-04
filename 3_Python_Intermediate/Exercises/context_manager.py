import datetime
import time
from contextlib import contextmanager


class ProcessTimer:
    def __init__(self):
        self.start = None
        self.stop = None
        self.difference = None

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = datetime.datetime.now()
        self.difference = self.stop - self.start

        print(self.difference)


@contextmanager
def process_timer():
    start = datetime.datetime.now()
    yield start
    stop = datetime.datetime.now()
    difference = stop - start
    print(difference)


with ProcessTimer() as t:
    print("class", t)
    time.sleep(1)

with process_timer() as t:
    print("function", t)
    time.sleep(2)
