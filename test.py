import time

def show_time():
    def inner():
        start = time.time()
        time.sleep(1)
        end = time.time()
        print('spend %s' % (end - start))
    # return inner
    print(inner)

show_time()