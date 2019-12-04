import time
from multiprocessing import Process, Pipe

class test():
    def __init__(self, name, age):
        self.name = name
        self.age = age

def send1(conn):
    n=0
    c = test("zhaoran",29)
    while True:
        n+=1
#       conn.send("send1: %d"%n)
        conn.send(c)
        time.sleep(0.1)
    conn.close()

def send2(conn):
    n=0
    while True:
        n+=1
        conn.send("send2: %d"%n)
        time.sleep(1.0)
    conn.close()

father_conn,son_conn=Pipe()
#p=[Process(target=send1,args=(son_conn,)),Process(target=send2,args=(son_conn,))]
p=[Process(target=send1,args=(son_conn,))]

p[0].start()
#p[1].start()

while True:
    print(father_conn.recv().age)
    time.sleep(2)

p[0].join()
#p[1].join()
