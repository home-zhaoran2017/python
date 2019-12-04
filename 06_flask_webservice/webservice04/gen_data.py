import pandas as pd

data = {'stu_no': ['S201907001', 'S201907002', 'S201907003', 'S201907004'],
        'name': ['王二', '张三', '李四', '赵五'],
        'register': ['0', '0', '1', '0'],
        'id_card': ['001', '002', '003', '004'],
        'is_card': ['0', '1', '0', '0'],
        'is_orphan': ['1', '0', '0', '0'],
        'is_martyr_child': ['0', '1', '0', '0'],
        'is_special_care': ['1', '0', '0', '0'],
        'is_low_income': ['0', '1', '0', '0'],
        'is_most_needy': ['0', '1', '0', '0'],
        'is_disability_stu': ['1', '0', '0', '0'],
        'disability_num': ['1', '0', '3', '0'],
        'unemployment_num': ['1', '2', '3', '0'],
        'family_income': ['6000', '5000', '6000', '7000'],
        'student_num': ['2', '1', '0', '2'],
        'older_num': ['1', '2', '0', '2'],
        'single_family': ['0', '1', '0', '0'],
        'serious_disaster': ['0', '1', '1', '0'],
        'natural_disasters': ['1', '0', '1', '1'],
        'sudden_accident': ['0', '1', '1', '1'],
        'house': ['1', '2', '0', '1']
        }

data = pd.DataFrame(data)

print(data.columns)
print(data.shape)

data.to_csv("data.txt",index=False,sep='|')
