#-*- coding=utf-8 -*-
import os
import sys
import time
import datetime
import pandas as pd
import psutil
from threading import Timer

root_path = os.path.dirname(os.path.realpath(__file__))
cmder="ps -eF | grep -v grep | grep python | grep engine | awk '{print $2}'"
pid = os.popen(cmder).readlines()
pid = [int(i.strip()) for i in pid]

cpuNum = psutil.cpu_count()
process = [psutil.Process(i) for i in pid]

def cpu_usage(process):
#   nowtime = str(datetime.datetime.today())[:19]
    cpu_all = psutil.cpu_percent()
    cpu_engine=0
    for p in process:
        cpu_engine+=p.cpu_percent()
    cpu_engine = cpu_engine/cpuNum
    
    return cpu_all, cpu_engine

def mem_usage(process):
#   nowtime = str(datetime.datetime.today())[:19]
    mem_usage = psutil.virtual_memory().percent
    mem = [0,0]
    for p in process:
        mem[0] += p.memory_info().rss/1024.0**2 # 单位: MB
        mem[1] += p.memory_percent()

    return mem[0], mem[1], mem_usage

def disk_usage(path):
#   nowtime = str(datetime.datetime.today())[:19]

    engine_usage=int(os.popen("du -s -b %s"%path).read().strip().split()[0])
    engine_usage = engine_usage / 1024.0**2 # 单位: MB
    
    disk_usage = psutil.disk_usage(path).percent
    disk_read = psutil.disk_io_counters().read_bytes # 单位: b
    disk_write = psutil.disk_io_counters().write_bytes # 单位: b

    return disk_usage, engine_usage, disk_read, disk_write

def net_usage():
#   nowtime = str(datetime.datetime.today())[:19]
    net_recv = psutil.net_io_counters().bytes_recv
    net_sent = psutil.net_io_counters().bytes_sent

    return net_recv, net_sent
    
def monitor():
    nowtime = str(datetime.datetime.today())[:19]
#   t1 = time.time(),time.clock()
    cpu = cpu_usage(process)
#   print("%s: %5.2f %5.2f"%cpu)

    mem = mem_usage(process)
#   print("%s: %5.2fMB %5.2f%% %5.2f%%"%mem)

    disk = disk_usage(root_path)
#   print("%s: %5.2f%% %5.2fMB %.2fb %.2fb"%disk)

    net = net_usage()
#   print("%s: %fb %fb"%net)

    res = [nowtime]+list(cpu)+list(mem)+list(disk)+list(net)
#   print(res)
    print("%s: %5.2f%% %5.2f%% %5.2fMB %5.2f%% %5.2f%% %5.2f%% %5.2fMB %.2fb %.2fb %.2fb %.2fb"%tuple(res))


    timer = Timer(1, monitor)
    timer.start()
    
#   t2 = time.time(),time.clock()
#   print(t2[0]-t1[0],t2[1]-t1[1])

monitor()
