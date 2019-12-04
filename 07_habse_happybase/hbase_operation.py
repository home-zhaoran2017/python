# -*- coding=utf-8 -*-
# Hbase operation
# Author: Department of Algorithm, THD.
# CreateTime: 2019-07-02; ModifyTime: 2019-09-04
#-- 导入模块 --------------------------------------
import sys
import time
import logging
import happybase
import json
import pandas as pd
import logging
import logging.config

from logger_conf import LOGGING_DIC
logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger("hbase")

#-- Hbase操作类 --------------------------------------
class HbaseOperation:
    def __init__(self,host):
        self.conn=happybase.Connection(host, autoconnect=False)

    #-- 获取数据库中已存在的表名 ------------------------
    def getTableNames(self):
        try:
            self.conn.open()
            return self.conn.tables()
        except Exception as e:
            logger.error(e)

    #-- 获取某个表的列名 ------------------------------
    def getTableColumns(self,table_name):
        try:
            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase!"%table_name)
                return

            table=self.conn.table(table_name)
            D=[]
            for rowkey, data in table.scan():
                D=data
                break
            if len(D)!=0:
                columns=list(D.keys())
                columns=[c[3:] for c in columns]
                return columns
            else:
                return D
        except Exception as e:
            logger.error(e)

    #-- 新建一个表 -----------------------------------
    def createTable(self, table_name):
        try:
            self.conn.open()
            if table_name in self.conn.tables():
                logger.warning("Table %s exists."%table_name)
            else:
                self.conn.create_table(
                    table_name,
                    {"cf":dict(max_versions=1)}
                )
        except Exception as e:
            logger.error(e)

    #-- 删除一个表 -----------------------------------------------
    def deleteTable(self, table_name):
        try:
            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase!"%table_name)
            else:
                self.conn.delete_table(table_name,disable=True)
        except Exception as e:
            logger.error(e)

    #-- 往指定表上传一条数据，需指定rowkey ----------------------
    def putRow(self,table_name,rowkey,data_dict):
        try:
            keys=data_dict.keys()
            for key in keys:
                data_dict["cf:"+key]=data_dict.pop(key)

            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            table.put(rowkey,data_dict)
        except Exception as e:
            logger.error(e)

    #-- 下载指定多个rowkeys的数据到文件中 ---------------------------
    def getRowstoFile(self, table_name, rowkeys, file_path):
        try:
            col=self.getTableColumns(table_name)
            self.conn.open()

            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            with open(file_path,'w') as f:
                f.write("%s\n"%('|'.join(col)))
                for rowkey, data in table.rows(rowkeys):
                    s=[]
                    for value in data.values():
                        s.append(value)
                    f.write("%s\n"%('|'.join(s)))
        except Exception as e:
            logger.error(e)

    #-- 获取一条指定rowkey的数据到字典 -----------------------------
    def getRow(self,table_name,rowkey,columns=None):
        try:
            if columns is not None:
                columns=["cf:"+f for f in columns]

            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            row = table.row(rowkey, columns=columns)
            keys=[c[3:] for c in row.keys()]
            values=row.values()
            row = dict(zip(keys,values))
            return row 
        except Exception as e:
            logger.error(e)

    def getRows():
        pass

    #-- 删除一条指定rowkey的数据 -----------------------------------------------
    def deleteRow(self,table_name,rowkey):
        try:
            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            table.delete(rowkey) 
        except Exception as e:
            logger.error(e)

    #-- 删除多条指定rowkey的数据 -----------------------------------------------
    def deleteRows(self, table_name, rowkeys, batch_size=1000):
        try:
            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            b = table.batch()
            t1=time.time()
            for n, row in enumerate(rowkeys):
                b.delete(row)
                if (n+1) % batch_size == 0:
                    b.send()
                    t2=time.time()
                    print("%d %.4f"%(n+1,t2-t1))
                    t1=time.time()
                sys.stdout.flush()
            b.send()
        except Exception as e:
            logger.error(e)
    
    #-- 将一个pandas.dataframe数据推送到hbase的指定表中 -----------------------
    def putTable(self,table_name,rowkeys,data_frame,batch_size=1000):
        try:
            data_frame=pd.DataFrame(data=data_frame,dtype=str)
            col=data_frame.columns
            col=["cf:"+c for c in col]
            data_frame.columns=col
            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)

            with table.batch(batch_size) as b:
                for n, row in enumerate(rowkeys):
                    print(n)
                    b.put(row,dict(data_frame.iloc[n,:])) 
        except Exception as e:
            logger.error(e)

    #-- 将一个pandas.dataframe数据推送到hbase的指定表中(建议该方法) -----------------------
    def putTable2(self, table_name, rowkeys, data_frame, batch_size=1000):
        try:
            data_frame=pd.DataFrame(data=data_frame,dtype=str)
            col=data_frame.columns
            col=["cf:"+c for c in col]
            data_frame.columns=col

            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            b = table.batch()
            t1=time.time()

            for n, row in enumerate(rowkeys):
                b.put(row, dict(data_frame.iloc[n,:]))
                if (n+1) % batch_size == 0:
                    b.send()
            b.send()

            t2=time.time()
            logger.info("dataframe size: %d; total time: %.4f s"%(data_frame.shape[0],t2-t1))
        except Exception as e:
            logger.error(e)

    #-- 获取指定表中的所有数据到dataframe，速度较慢，建议小数据量时使用----------------------------
    def getTable(self,table_name,columns=None):
        try:
            if columns is not None:
                columns=["cf:"+c for c in columns]

            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)
            D=['"%s":%s'%(key,json.dumps(data)) for key, data in table.scan(columns=columns)]
            D="{%s}"%','.join(D)
            D=pd.read_json(D,convert_axes=False,dtype=object)
            col=D.index
            col=[c[3:] for c in col]
            D=pd.DataFrame(D.values.T,index=D.columns,columns=col)
            return D
        except Exception as e:
            logger.error(e)

    #-- 获取指定表中的所有数据到文件中，速度较快，建议大数据量时使用 --------------------------
    def getTabletoFile(self,table_name,file_path,columns=None, date_start=None, date_stop=None):
        try:
            if columns is None:
                col = self.getTableColumns(table_name)
            else:
                col = columns
                columns=["cf:"+c for c in columns]

            if date_start==None:
                row_start=None
            else:
                row_start=str(time.mktime(time.strptime(date_start, "%Y-%m-%d")))

            if date_stop==None:
                row_stop=None
            else:
                row_stop=str(time.mktime(time.strptime(date_stop, "%Y-%m-%d")))

            self.conn.open()
            if table_name not in self.conn.tables():
                logger.warning("Table %s not exist in hbase."%table_name)
                return

            table=self.conn.table(table_name)

            t1=time.time()
            with open(file_path,'w') as f:
                f.write("%s\n"%('|'.join(col)))
                num=0
                for rowkey, data in table.scan(columns=columns,row_start=row_start, row_stop=row_stop):
                    s=[]
                    for value in data.values():
                        s.append(value)
                    f.write("%s\n"%('|'.join(s)))
                    num+=1

            t2=time.time()
            logger.info("Get table: %s; data num: %d; total time: %.4f s"%(table_name, num, t2-t1))
        except Exception as e:
            logger.error(e)
