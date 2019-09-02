from threading import Timer, activeCount

def print_hello():
    print("hello,world!")
    timer = Timer(2, print_hello)
    timer.start()
    print(activeCount())

print_hello()
