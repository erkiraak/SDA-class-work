from datetime import datetime


def disable_at_night(time_from=00, time_to=12):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if time_from <= datetime.now().hour < time_to:
                func(*args, **kwargs)
            else:
                print("Welcome to KLM airlines")
        return wrapper
    return outer_wrapper


@disable_at_night(1, 12)
def say_something(string):
    print(string)


say_something("tere")
