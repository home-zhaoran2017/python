# -*- coding: utf-8 -*-
import pandas as pd

def clean_data(family_info):
        data = pd.DataFrame(family_info,index=[0])
        data = data.astype({'is_card': 'int', 'is_orphan': 'int', 'is_martyr_child': 'int', 'is_special_care': 'int',
                            'is_low_income': 'int', 'is_most_needy': 'int', 'is_disability_stu': 'int',
                            'disability_num': 'int', 'unemployment_num': 'int', 'family_income': 'int',
                            'student_num': 'int', 'older_num': 'int', 'single_family': 'int', 'serious_disaster': 'int',
                            'natural_disasters': 'int', 'sudden_accident': 'int', 'house': 'int'
                            })
        return data


def edge_family_score(family_info):
        data = clean_data(family_info)
        # 依据家庭残疾人数计算学生得分
        if data['disability_num'][0] >= 2:
            disability_num_score = 10
        else:
            if data['disability_num'][0] == 1:
                disability_num_score = 5
            else:
                disability_num_score = 0
        # print(disability_num_score)

        # 依据家庭失业人数计算学生得分
        if data['unemployment_num'][0] >= 2:
            unemployment_num_score = 10
        else:
            if data['unemployment_num'][0] == 1:
                unemployment_num_score = 5
            else:
                unemployment_num_score = 0
        # print(unemployment_num_score)

        # 依据家庭人均收入计算学生得分
        if data['family_income'][0] <= 5000:
            family_income_score = 10
        else:
            if data['family_income'][0] <= 10000:
                family_income_score = 5
            else:
                family_income_score = 0
        # print(family_income_score)

        # 依据家庭就学人数计算学生得分
        if data['student_num'][0] >= 2:
            student_num_score = 10
        else:
            if data['student_num'][0] == 1:
                student_num_score = 5
            else:
                student_num_score = 0
        # print(student_num_score)

        # 依据家庭赡养人数计算学生得分
        if data['older_num'][0] >= 2:
            older_num_score = 10
        else:
            if data['older_num'][0] == 1:
                older_num_score = 5
            else:
                older_num_score = 0
        # print(older_num_score)

        # 依据单亲家庭计算学生得分
        if data['single_family'][0] >= 2:
            single_family_score = 10
        else:
            if data['single_family'][0] == 1:
                single_family_score = 5
            else:
                single_family_score = 0
        # print(single_family_score)

        # 依据重大疾病计算学生得分
        if data['serious_disaster'][0] == 1:
            serious_disaster_score = 10
        else:
            serious_disaster_score = 0
        # print(serious_disaster_score)

        # 依据自然灾害计算学生得分
        if data['natural_disasters'][0] == 1:
            natural_disasters_score = 10
        else:
            natural_disasters_score = 0
        # print(natural_disasters_score)

        # 依据突发事故计算学生得分
        if data['sudden_accident'][0] == 2:
            sudden_accident_score = 10
        else:
            if data['sudden_accident'][0] == 1:
                sudden_accident_score = 5
            else:
                sudden_accident_score = 0
        # print(sudden_accident_score)

        # 依据房屋情况计算学生得分
        if data['house'][0] == 0:
            house_score = 10
        else:
            if data['house'][0] == 1:
                house_score = 6
            else:
                if data['house'][0] == 2:
                    house_score = 3
                else:
                    house_score = 0
        # print(house_score)

        family_score = disability_num_score + unemployment_num_score + family_income_score + student_num_score + \
                       older_num_score + single_family_score + serious_disaster_score + natural_disasters_score + \
                       sudden_accident_score + house_score
        return family_score


def calculate_family_score(family_info):
        data = clean_data(family_info)
        special_num = data[['is_orphan', 'is_martyr_child', 'is_special_care', 'is_low_income', 'is_most_needy',
                            'is_disability_stu']].apply(lambda x: x.sum(), axis=1)
        data['special_num'] = special_num
        # print(data)

        if data[data['is_card'] == 1].empty is False:
            data['family_score'] = 100
            print(data)
        else:
            if data[data['special_num'] >= 2].empty is False:
                data['family_score'] = 100
            if data[data['special_num'] == 1].empty is False:
                data['family_score'] = 50 + edge_family_score(data)
            if data[data['special_num'] == 0].empty is False:
                data['family_score'] = edge_family_score(data)

        if data[data['family_score'] > 100].empty is False:
            data['family_score'] = 100

        return data[['stu_no', 'family_score']]


if __name__ == '__main__':
    # 模拟数据
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
    score = calculate_family_score(data)
    print(score)
