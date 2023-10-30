# decorator use case 2
import datetime


def log(func):
    ""
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write("\n" + str(func) + " Function call with " + " ".join([str(arg) for arg in args]) +\
                    " at " + str(datetime.datetime.now()))
            temp = func(*args, **kwargs)
            return temp
    return wrapper


@log
def summation(a, b):  # introduce a para to the function
    return a + b


summation(9, 9)
