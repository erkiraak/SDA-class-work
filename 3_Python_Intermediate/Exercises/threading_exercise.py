import threading
import time
import random

int_list = [random.randint(0, 100) for _ in range(100)]
sorted_list_ascending = []
sorted_list_descending = []
processes = []


def sleep_sort_ascending(integer):
    time.sleep(0.1 * integer)
    sorted_list_ascending.append(integer)


def sleep_sort_descending(integer):
    time.sleep(0.1 * (max(int_list) - integer))
    sorted_list_descending.append(integer)


for number in int_list:
    td = threading.Thread(target=sleep_sort_descending, args=(number,))
    td.start()
    processes.append(td)

for t in processes:
    t.join()

processes.clear()

for number in int_list:
    ta = threading.Thread(target=sleep_sort_ascending, args=(number,))
    ta.start()
    processes.append(ta)

for t in processes:
    t.join()

print(sorted_list_ascending)
print(sorted_list_descending)
print(sorted_list_descending == sorted_list_ascending[::-1])
