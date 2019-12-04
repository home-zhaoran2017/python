# -*- coding: utf-8 -*-
import time
import sys
import requests

# url = "http://localhost:5000/"
# response = requests.get(url)

# 打印状态码
# print(response.status_code)

# json格式打印get内容
# print(response.text)

# put 一条数据
while True:
        data = {'stu_no': '201907001',
                'name': '王二',
                'register': '0',
                'id_card': '001',
                'is_card': '0',
                'is_orphan': '0',
                'is_martyr_child': '0',
                'is_special_care': '0',
                'is_low_income': '0',
                'is_most_needy': '0',
                'is_disability_stu': '1',
                'disability_num': '1',
                'unemployment_num': '1',
                'family_income': '6000',
                'student_num': '2',
                'older_num': '1',
                'single_family': '2',
                'serious_disaster': '0',
                'natural_disasters': '1',
                'sudden_accident': '0',
                'house': '1'
                }

        url = "http://192.168.3.109:5000/put/"
        response = requests.get(url)
        res = requests.put(url, json=data)
        print(res.text)
        # time.sleep(0.01)
        # break
        sys.stdout.flush()
