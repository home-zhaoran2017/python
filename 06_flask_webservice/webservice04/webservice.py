#-*- coding=utf-8 -*-
import json
import datetime
from flask import Flask
from flask import jsonify
from flask import request
from family_score import calculate_family_score
from family_score import clean_data

app = Flask(__name__)

@app.route('/family_calculate',methods=["POST"])
def createDB():
    DB={}
    try:
        stu_info=request.args.get("stu_info")
        stu_info=json.loads(stu_info)
        keys=list(stu_info.keys())
        values=list(stu_info.values())
        keys=[s.encode("utf-8") for s in keys]
        values=[s.encode("utf-8") for s in values]
        stu_info=dict(zip(keys,values))
        DB["stu_no"]=stu_info["stu_no"]
    except:
        DB["stu_no"]="unknown"

    try:
        # 计算得分
        score = calculate_family_score(stu_info)
        DB["score"] = score["family_score"].values[0]

        # 推送到数据库
        score.to_csv("score.txt",index=False,sep='|',header=None,mode='a')

        # 显示成功状态
        DB["status"] = "SUCCESS"
    except:
        DB["score"] = "unknown"
        # 显示失败状态
        DB["status"] = "FAILED"

    DB["datetime"]=str(datetime.datetime.today())[:19]
    return jsonify(DB)

if __name__ == '__main__':
 app.run(host="192.168.3.104", port=5000)
