#-*- coding=utf-8 -*-
import json
import requests

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
json_str = json.dumps(data)

url = "http://192.168.3.104:5000/family_calculate?stu_info="+json_str
res = requests.post(url)
print(res.text)
