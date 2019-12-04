#-*- coding=utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from family_score import calculate_family_score

app = Flask(__name__)

stu_info = {
    'stu_no': ['S201907001'],
    'name': ['王二'],
    'register': ['0'],
    'id_card': ['001'],
    'is_card': ['0'],
    'is_orphan': ['1'],
    'is_martyr_child': ['0'],
    'is_special_care': ['1'],
    'is_low_income': ['0'],
    'is_most_needy': ['0'],
    'is_disability_stu': ['1'],
    'disability_num': ['1'],
    'unemployment_num': ['1'],
    'family_income': ['6000'],
    'student_num': ['2'],
    'older_num': ['1'],
    'single_family': ['0'],
    'serious_disaster': ['0'],
    'natural_disasters': ['1'],
    'sudden_accident': ['0'],
    'house': ['1']
}

DB = { 
    "status":"FAILED",
    "stu_info":stu_info
}
        

@app.route('/',methods=['GET'])
def getAllEmp():
    return DB

@app.route('/put/',methods=["PUT"])
def createEmp():
    DB["stu_info"]=request.json
    try:
        score = calculate_family_score(DB["stu_info"])  
        score.to_csv("score.txt",index=False,sep='|')
        DB["status"]="SUCCESS"
    except:
        DB["status"]="FAILED"

    return DB["status"]

if __name__ == '__main__':
 app.run(host="192.168.3.104")
