## hbase的基本操作

0. 连接数据库

```python
# 导入模块
from hbase_operation import HbaseOption

# 定义hbase数据库地址
host="192.168.3.128"
# 连接数据库
hopt = HbaseOption(host)
```

1. 获取数据库中的所有表名
    ```python
    hopt.getTableNames()
    ```

2. 获取某个表对应的字段列表
    ```python
    hopt.getTableColumns(table_name)
    ```

3. 新建一个表
    ```python
    hopt.createTable(table_name)
    ```

4. 删除一个表
    ```python
    hopt.deleteTable(table_name)
    ```

5. 往某个表中推送指定rowkey的一条数据

    推送的单条数据必须是字典数据类型，字典的key和value需是字符串类型。rowkey是对应的数据索引，也是字符串类型。
    ```python
    hopt.putRow(table_name,rowkey,data_dict)
    ```

6. 从某个表中获取指定rowkey的一条数据
    ```python
    hopt.getRow(table_name,rowkey)
    ```

7. 推送DataFrame数据到某个表中

    要推送的表以pandas的dataframe类型表示，数据可不必是字符串类型，方法中会进行转换，由于表中存在多条数据，所有的rowkey放到列表中作为参数传递。
    ```python
    hopt.putTable(table_name,rowkeys,dataframe,batch_size=1000)
    ```

8. 下载整个表到DataFrame中

    将整个hbase表下载下来，并转换成dataframe数据类型，大数据量时下载较慢，该方法需要进行优化。
    ```python
    hopt.getTable(table_name)
    ```

9. 下载整个表到本地文件中(速度更快)
    ```python
    hopt.getTabletoFile(table_name,file_path)
    ```

10. 下载指定rowkeys的数据到文件中
    ```python
    hopt.getRowstoFile(table_name,rowkeys,file_path)
    ```

11. 下载指定rowkey对应的列的数据 
    ```python
    hopt.getFieldbyRow(table_name,rowkey,fields)
    ```
    `--fields`: **list object**
