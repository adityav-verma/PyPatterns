import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'Time taken by function {int(end - start) * 1000}ms')
        return result
    return wrapper


@time_it
def do_work():
    print('Starting work')
    time.sleep(1)
    print('Completed work')


if __name__ == '__main__':
    do_work()
