import datetime
from context_manager import ProcessTimer, process_timer


def run_between(start, stop):
    def outer(func):
        def wrapper(*args, **kwargs):
            if start < datetime.datetime.now().hour < stop:
                print(datetime.datetime.now().strftime("%H:%M:%S:%f"))
                func(*args, **kwargs)
                print(datetime.datetime.now().strftime("%H:%M:%S:%f"))
            else:
                return f"Can only be run between {start} and {stop}"

        return wrapper

    return outer


@run_between(10, 22)
def work_call(name):
    print(f"{name} called " + "ring" * 10000)


with ProcessTimer() as time:
    print("class", time)
    print(work_call("Arno"))

with process_timer() as time:
    print("function" + time)
    print(work_call("Arno"))
