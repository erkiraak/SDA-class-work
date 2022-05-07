def capitalize(func):
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        return name.title()

    return wrapper
