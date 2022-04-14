from functools import wraps


class Cloud:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Connected to cloud")
        self.func()
        print("Connection to cloud Closed")


@Cloud
def upload_file():
    print("Uploading File....")


def debug(func):
    func_name = func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func_name)
        return func(*args, **kwargs)

    return wrapper


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@debug
def p():
    print()


if __name__ == '__main__':
    upload_file()
    p()
