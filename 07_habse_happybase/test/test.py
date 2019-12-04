import time
import random
import numpy as np
import pandas as pd
from hbase_operation import HbaseOperation

host = "192.168.3.41"
hopt = HbaseOperation(host)
#print(hopt.getTableColumns("ai_stu_info_test"))

hopt.getTabletoFile("ai_cost_test","out.txt", date_start="2019-04-01", date_stop="2019-04-09")

#for table in hopt.getTableNames():
#    print(table)

#data = pd.read_csv("cost",header=None,sep='|',dtype=object)
#data.columns=["stu_no","cost_place","cost_type","cost_money","cost_datetime"]

#rowkeys=[None]*data.shape[0]

#for n, v in enumerate(data[["stu_no","cost_datetime"]].values):
#    rowkey = str(int(time.mktime(time.strptime(v[1], "%Y-%m-%d %H:%M:%S")))) + v[0] + str(random.randint(0,9))
#    rowkeys[n]=rowkey


#hopt.putTable2("ai_cost_test",rowkeys,data)
