# pcpp1 practice: timestamping logger
# decorators, datetime module

from datetime import datetime

def timestamper(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
        timestamp = datetime.now()
        string_ts = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print(f'Evaluated at {string_ts}')
        print('')
    return wrapper


@timestamper
def add(num1, num2):
    return num1 + num2

@timestamper
def subtract(num1, num2):
    return num1 - num2

# testing
add(1, 2)
add(7, 10)
subtract(4, 3)
subtract(10, 2)