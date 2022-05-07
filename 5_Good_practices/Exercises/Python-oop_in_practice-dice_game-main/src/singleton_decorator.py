def Singleton(class_):
    __instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return get_instance