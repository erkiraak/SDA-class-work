import datetime


def singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]

    return get_instance


@singleton
class Counter:
    def __init__(self, filename):
        self.filename = filename

    def add_string(self, string):
        write_string = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " - " + string

        try:
            log_file = open(self.filename, "a")
        except FileNotFoundError:
            log_file = open(self.filename, "w")
        finally:
            log_file.write(write_string + "\n")
            log_file.close()


counter = Counter("singleton_testing.txt")
counter.add_string("tere")
counter2 = Counter("singleton_testing2.txt")
counter2.add_string("hommikust")
