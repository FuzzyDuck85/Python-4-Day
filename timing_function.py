import time

def timing_function(callback):
    def wrapper():
        time1 = time.time() # before function call
        callback()
        time2 = time.time() # after function call
        return f"here is how long it took: {time2 - time1} seconds"

    return wrapper
