import os
import time
import datetime

from multiprocessing import Process, Lock
from multiprocessing.managers import BaseManager


class test():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return self.name, self.age

    def increase(self, x):
        self.age += x

def t1(lock, c, x):
    with lock:
        c.increase(x)

def myManager(name, cls):
    BaseManager.register(name, cls)
    m = BaseManager()
    m.start()
    return m

if __name__=="__main__":
    manager = myManager("test", test)
    c = manager.test("zhaoran",29)

    print(c.get_data())

    lock = Lock()
    p = Process(target=t1, args=(lock, c, 1))
    p.start()
    p.join()

    print(c.get_data())
